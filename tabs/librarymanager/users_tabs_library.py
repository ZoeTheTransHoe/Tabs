# users_tabs.py
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
from multiprocessing.managers import DictProxy

from gi.repository import Adw, Gio, GLib, Gtk, Pango

class UsersTabsLibrary():
    """
    Holds dictionary of users tabs, and methods for interacting with users library of tabs.
    """
    __gtype_name__ = 'UsersTabs'

    users_library = {"My Tab 1":["Myself","Peak Album"],"My Tab 2":["Myself","Peak Album 2"],
                     "Jesus of Suburbia":["Green Day","American Idiot"],"21 Guns":["Green Day","21 Century Breakdown"],
                     "Lonely Day":["System Of A Down","Hypnotize"],"Aerials":["System Of A Down","Toxicity"],
                     "Would?":["Alice In Chains","Dirt"],
                     "Money?":["Pink Floyd","The Dark Side Of The Moon"],
                     "Anchor":["Thank You Scientist","Terraformer"]}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def tabs_been_added(self):
        """
        Checks if there are any user-added tabs.
        Returns: Boolean
        """
        if self.number == 0:
            return False
        else:
            return True

    @property
    def number(self):
        """
        Gets Number Of Tabs In Users Library
        Returns: Int
        """
        return len(self.users_library)

    @property
    def artists(self):
        """
        Returns a list of all artists in users library and the number of times they appear.
        Returns: Dict
        """

        artists_dict = {}
        for keys in self.users_library:
            current_artists = self.users_library.get(keys)[0]
            if self.users_library.get(keys)[0] in artists_dict:
                artist_count = artists_dict.get(current_artists) + 1
                artists_dict.update({self.users_library.get(keys)[0]: artist_count})
            else:
                artists_dict.update({self.users_library.get(keys)[0] : 1})

        #Sorts Dictionary (Except Myself) In Alphabetical Order,
        keys_list = list(artists_dict.keys())
        keys_list.remove("Myself")
        keys_list.sort()
        artists_dict_sorted = {i: artists_dict[i] for i in keys_list}

        if "Myself" in artists_dict:
            artists_dict_sorted = {"Myself": artists_dict["Myself"]} | artists_dict_sorted

        return artists_dict_sorted

    def search_artists_tabs(self, search_artist) -> list[list[str]]:
        """
        Searches the users library for a given artist, and returns a 2D List of all tabs under that artist, with each
        Sublist containing the given tabs song and album name for that tab.
        Arg:
            search_artist: Str
        Returns: 2D List
        """

        artist_tabs_info = []
        for keys in self.users_library:
            if self.users_library[keys][0] == search_artist:
                artist_tabs_info.append([keys,self.users_library[keys][1]])

        return artist_tabs_info


