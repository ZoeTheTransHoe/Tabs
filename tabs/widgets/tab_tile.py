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

from gi.repository import Gtk

@Gtk.Template(resource_path='/org/zoey/Tabs/../data/ui/tab_tile.ui')
class TabTile(Gtk.FlowBoxChild):
    __gtype_name__ = "TabTile"

    tile_album_cover = Gtk.Template.Child()
    tile_title = Gtk.Template.Child()
    tile_album_name = Gtk.Template.Child()

    def __init__(self) -> None:
        """
        Creates a Gtk FlowBoxChild with an Image for the album cover and
        2 labels, one for song name + artist, and one for album name

        No args.
        """
        super().__init__()

    def add_tile_data(self, new_song_name, new_artist_name, new_album_name) -> None:
        """
        Populates a tile with the information needed.
        Args:
            new_song_name, new_artist_name, new_album_name: str
        """
        self.tile_album_name.set_text(new_album_name)
        title = new_song_name + " - " + new_artist_name
        self.tile_title.set_text(title)

