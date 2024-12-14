# window.py
#
# Copyright 2024 zoey
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gio, GLib, Gtk, Pango
from .libraryui import LibraryUI
from .create_tab_library import CreateTabLibrary
from .users_tabs_library import UsersTabsLibrary

@Gtk.Template(resource_path='/org/zoey/Tabs/../data/ui/welcome.ui')
class TabsWelcome(Adw.ApplicationWindow):
    """Welcome Window"""
    __gtype_name__ = 'TabsWindow'

    ### Buttons ###
    #Button Box
    welcome_button_box = Gtk.Template.Child()
    #Individual Buttons
    download_tabs_button = Gtk.Template.Child()
    create_new_tab_button = Gtk.Template.Child()
    # Menu Button
    open_button = Gtk.Template.Child()

    ### Sidebar ###
    split_view = Gtk.Template.Child()
    sidebar_list = Gtk.Template.Child()
    #Labels
    all_tabs_count_label = Gtk.Template.Child()
    all_artists_label = Gtk.Template.Child()

    ### Welcome Status Page ###
    welcome_status = Gtk.Template.Child()

    ### Main Library Of Tabs###
    library =  Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("welcome.py/TabsWelcome Loaded")

        #Action that opens a file picker accepting either a JSON or MusicXML file to load into app.
        open_tab_action = Gio.SimpleAction(name="open")
        open_tab_action.connect("activate", self.open_tabs_file)
        self.add_action(open_tab_action)

        # TODO - Opens New window to download tabulatures from somewhere idk.
        download_tab_action = Gio.SimpleAction(name="download")
        download_tab_action.connect("activate", self.download_tab)
        self.add_action(download_tab_action)

        # TODO - Opens window to create a new blank tab
        create_tab_action = Gio.SimpleAction(name="create")
        create_tab_action.connect("activate", self.create_tabs_file)
        self.add_action(create_tab_action)

        # Hides sidebar button
        hide_sidebar_action = Gio.SimpleAction(name="hide_sidebar")
        hide_sidebar_action.connect("activate", self.toggle_sidebar)
        self.add_action(hide_sidebar_action)

        # Hides sidebar button
        fullscreen_action = Gio.SimpleAction(name="set_fullscreen")
        fullscreen_action.connect("activate", self.set_fullscreen)
        self.add_action(fullscreen_action)

        # Search button
        search_action = Gio.SimpleAction(name="search")
        search_action.connect("activate", self.search)
        self.add_action(search_action)

        # Open Support Tabs Kofi :)
        support_tabs_action = Gio.SimpleAction(name="support_tabs")
        support_tabs_action.connect("activate", self.support_tabs)
        self.add_action(support_tabs_action)

        # Calls Methods to Populate Window With Content Where Needed
        user_tabs_library = UsersTabsLibrary()
        self.add_sidebar_buttons(user_tabs_library)
        self.create_tabs_library(user_tabs_library)

    ### Open XML Tab File Methods ###
    def open_tabs_file(self, action, _):
        """Open a MusicXML or JSON file using file picker."""
        xml_file = Gtk.FileDialog()
        xml_file.open(self, None, self.open_tabs_file_response)

    def open_tabs_file_response(self, dialog, result):
        """
        Tries to send whatever file chosen to processing if a user selects a file
        and blows up the user if they do not pick a file
        Args:
            result: Either the file the user choose or an error if they do not pick a file.
        """
        try:
            file = dialog.open_finish(result)
            self.process_xml(file)
        except GLib.GError:
            print("Blows u up")

    def process_xml(self, file):
        """ Process XML File"""
        print(file)
        pass

    ### Sidebar methods###
    def toggle_sidebar(self, action, _):
        """ Reverses visibility status of sidebar"""
        toggle_status = self.split_view.get_show_sidebar()
        self.split_view.set_show_sidebar(not toggle_status)

    def add_sidebar_buttons(self, user_tabs_object):
        """
        Populate Sidebar with [All Tabs], [Popular Tabs], and Artists category underneath
        Arg:
            user_tabs_object: UsersTabsLibrary()
        Return: True/False if the
        """
        try:
            # Sets Artist label to invisible if the user has no tabs in their library
            self.all_artists_label.set_visible(user_tabs_object.tabs_been_added())
            self.all_tabs_count_label.set_label(str(user_tabs_object.number))

            # Loops every artist and adds a new widget to the sidebar list
            sidebar_buttons = LibraryUI()
            for keys in user_tabs_object.artists:
                if keys == "Myself":
                    new_button = sidebar_buttons.create_sidebar_button("pencil-symbolic", keys, user_tabs_object.artists[keys])
                else:
                    new_button = sidebar_buttons.create_sidebar_button("people-symbolic", keys, user_tabs_object.artists[keys])
                self.sidebar_list.append(new_button)
            return True
        except:
            raise Exception

    ### Welcome Window Library Methods ###
    def create_tabs_library(self, user_tabs_object):
        """
        Creates users library of tabs as a row. See "Welcome Page (Tabs Already Added)" on Figma for what this should look like.
        """
        if user_tabs_object.tabs_been_added():
            #If there are any user added tabs, set Welcome Status as invisible and library to visible
            self.welcome_status.set_visible(False)
            self.library.set_visible(True)
        pass

    ### Search Methods ###
    def search(self, action, _):
        print("Searching...")
        pass

    ### Other Methods ###
    def download_tab(self, action, _):
        ''' Litteraly Just Prints Downloading For Now'''
        print("Downloading...")

    def create_tabs_file(self, action, _):
        """Litteraly Just Prints Create Window"""
        print("Create Window")

    def set_fullscreen(self, action, _):
        """Asks to reverse fullscreen status when clicked"""
        try:
            if self.is_fullscreen():
                self.unfullscreen()
                return
            else:
                self.fullscreen()
        except:
            print("Issue Fullscreening!") #TODO - Use Adw.Toast for this

    def support_tabs(self, action, _):
        Gio.AppInfo.launch_default_for_uri("https://ko-fi.com/zoeyahmed")
        pass

