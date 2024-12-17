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
from .users_tabs_library import UsersTabsLibrary

@Gtk.Template(resource_path='/org/zoey/Tabs/../data/ui/artist_sidebar.ui')

class ArtistSidebar(Gtk.ListBoxRow):
    __gtype_name__ = 'ArtistSidebar'

    users_library = UsersTabsLibrary()

    ### Boxes ###
    artist_box = Gtk.Template.Child()
    ### Labels ###
    artist_name_label = Gtk.Template.Child()
    artist_count_label = Gtk.Template.Child()
    ### Icons ###
    artist_icon = Gtk.Template.Child()

    def __init__(self, **kwargs) -> None:
        """
        Creates a GtkBox with icon, artist name and number of tabs by that artist
        To be appended to the sidebar as a GtkListRow .
        No args or return.
        """
        super().__init__(**kwargs)

    def add_sidebar_data(self, icon, artist_name, artists_number):
        """
        Adds needed data to make sidebar
        Args:
        icon, artist_name: Str
        artists_number: Int
        """
        #Name Of Artist E.g. David Bowie, Linkin Park, Myself
        try:
            self.artist_name_label.set_text(artist_name)
        except:
            raise TypeError("Artist Name Must Be A Str!")

        #Icon - Either pencil-symbolic for "Myself" or people-symbolic for other artists
        try:
            self.artist_icon.set_from_icon_name(icon)
        except:
            raise TypeError("Icon Name Must Be A Str!")

        #Aritst Number - Must be more than 1 e.g 5, 69
        try:
            if artists_number <= 0:
                raise ValueError("Artist Number must be more than 0!")
            else:
                self.artist_count_label.set_text(str(artists_number))
        except:
            raise TypeError("Artist Number Must be An Int!")

    def