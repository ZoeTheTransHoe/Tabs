# main.py
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

import sys
import os
import gi
from time import sleep

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .welcome import TabsWelcome

class TabsApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        if os.getenv("XDG_CURRENT_DESKTOP") == "COSMIC":
            Gio.AppInfo.launch_default_for_uri("https://stopthemingmy.app")
            self.quit()

        super().__init__(application_id='org.zoey.Tabs',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)
        self.create_action('quit', lambda *_: self.quit(), ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action, ['<primary>comma'])

        #My Own Keyboard Shortcuts (Shove it).
        self.set_accels_for_action('win.open', ['<primary>o'])
        self.set_accels_for_action('win.download', ['<primary>d'])
        self.set_accels_for_action('win.create', ['<primary><Alt>n'])
        self.set_accels_for_action('win.hide_sidebar', ['F9'])
        self.set_accels_for_action('win.set_fullscreen', ['F11'])
        self.set_accels_for_action('win.search', ['<primary>s'])

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = TabsWelcome(application=self)
        win.present()
    def on_about_action(self, *args):
        """Callback for the app.about action."""
        about = Adw.AboutDialog(application_name='Tabs',
                                application_icon='org.zoey.Tabs',
                                developer_name='Zoey Ahmed',
                                version='0.1.0',
                                developers=['Zoey Ahmed'],
                                copyright='© 2024 Zoey Ahmed')
        # Translators: Replace "translator-credits" with your name/username, and optionally an email or URL.
        about.set_translator_credits(_('translator-credits'))
        about.present(self.props.active_window)

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """The application's entry point."""
    app = TabsApplication()
    return app.run(sys.argv)
