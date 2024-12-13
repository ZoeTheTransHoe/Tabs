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
from .sidebar import Sidebar
from .create_tab_library import CreateTabLibrary
from .users_tabs import UsersTabs

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

    ### Welcome Status Page ###
    welcome_status = Gtk.Template.Child()

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

        # Calls Methods to Populate Window With Content Where Needed
        user_tabs = UsersTabs()
        self.add_sidebar_buttons(user_tabs)
        self.create_tabs_library(user_tabs)

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
        """Populate Sidebar with [All Tabs], [Popular Tabs], and Artists category underneath"""
        if user_tabs_object.tabs_been_added() == True:
            all_tabs_button = Gtk.ListBoxRow()
            all_tabs_label = Gtk.Label()
            all_tabs_label.set_text("All Tabs")
            all_tabs_button.set_child(all_tabs_label)

            popular_tabs_button = Gtk.ListBoxRow()
            popular_tabs_label = Gtk.Label()
            popular_tabs_label.set_text("Popular Tabs")
            popular_tabs_button.set_child(popular_tabs_label)

            self.sidebar_list.append(all_tabs_button)
            self.sidebar_list.append(popular_tabs_button)
        pass

    ### Welcome Window Library Methods ###
    def create_tabs_library(self, user_tabs_object):
        """
        Creates users library of tabs as a row. See "Welcome Page (Tabs Already Added)" on Figma for what this should look like.
        """
        if user_tabs_object.tabs_been_added() == False:
            #If there are any user added tabs, set Welcome Status as invisible to be replaced with library
            self.welcome_status.set_visible(False)

            #Anchors Create/Download Button Row to bottom of screen
            self.welcome_button_box.set_valign(2)

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