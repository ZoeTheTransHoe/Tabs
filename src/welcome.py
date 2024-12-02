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

@Gtk.Template(resource_path='/org/zoey/Tabs/../data/ui/welcome.ui')
class TabsWelcome(Adw.ApplicationWindow):
    __gtype_name__ = 'TabsWindow'
    
    welcome_status = Gtk.Template.Child()

    ### Buttons ###
    download_tabs = Gtk.Template.Child()
    create_new_tab = Gtk.Template.Child()
    # Menu Button
    open_button = Gtk.Template.Child()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #TODO - Open a MusicXML or JSON file using file picker.
        #Action that opens a file picker accepting either a JSON or MusicXML file to load into app.
        open_tab_action = Gio.SimpleAction(name="open")
        open_tab_action.connect("activate", self.open_tabs_file)
        self.add_action(open_tab_action)

    def open_tabs_file(self, action, _):
        ''' Litteraly Just Prints Meow For Now'''
        print("Meow")