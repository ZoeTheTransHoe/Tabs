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

class LibraryUI(Gtk.ListBox):
    __gtype_name__ = 'TabSidebar'

    users_library = UsersTabsLibrary()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("sidebar.py/Sidebar Loaded")

    def create_sidebar_button(self, icon, artist_name, artists_number):
        """
        Creates a GtkBox with icon, artist name and number of tabs by that artist
        To be appended to the sidebar as a GtkListRow .
        Args:
            icon, artist_name: Str
            artists_number: Int
        Return: GtkWidget
        """
        #Box Of Widgets
        button_box = Gtk.Box()
        button_box.set_spacing(12)
        button_box.set_margin_bottom(12)
        button_box.set_margin_top(12)

        #Name Of Artist E.g. David Bowie, Linkin Park, Myself
        artist_name_label = Gtk.Label()
        try:
            artist_name_label.set_text(artist_name)
        except:
            raise TypeError("Artist Name Must Be A Str!")
        artist_name_label.set_halign(1)

        #Icon - Either pencil-symbolic for "Myself" or people-symbolic for other artists
        artist_icon = Gtk.Image()
        artist_icon.set_pixel_size(18)
        try:
            artist_icon.set_from_icon_name(icon)
        except:
            raise TypeError("Icon Name Must Be A Str!")

        #Aritst Number - Must be more than 1 e.g 5, 69
        artist_number_label = Gtk.Label()
        try:
            if artists_number <= 0:
                raise ValueError("Artist Number must be more than 0!")
            else:
                artist_number_label.set_text(str(artists_number))
        except:
            raise TypeError("Artist Number Must be An Int!")
        artist_number_label.set_halign(2)
        artist_number_label.set_hexpand(True)
        artist_number_label.set_hexpand_set(True)
        artist_number_label.add_css_class("dim-label")

        button_box.append(artist_icon)
        button_box.append(artist_name_label)
        button_box.append(artist_number_label)

        return button_box

    def create_sidebar_(self):
        pass