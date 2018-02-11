from __future__ import unicode_literals

import logging

from mopidy.core import CoreListener # pylint: disable=import-error

import pykka # pylint: disable=import-error

from .menu import BrowseMenu
from .painter import Painter
from .input import Input

logger = logging.getLogger(__name__)

class FrontPanel(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(FrontPanel, self).__init__()
        self.core = core
        self.menu = BrowseMenu(core)
        self.painter = Painter(core, self.menu)
        self.input = Input(self)

    def on_start(self):
        self.painter.start()

    def handle_input(self, input_key):
        #self.painter.print_text(input_key)

        if input_key == "play":
            self.core.playback.resume()
        elif input_key == "pause":
            self.core.playback.pause()
        elif input_key == "stop":
            self.core.playback.stop()
        elif input_key == "vol_up":
            pass
        elif input_key == "vol_down":
            pass
        elif input_key == "next":
            self.menu.next()
        elif input_key == "prev":
            self.menu.prev()
        elif input_key == "select":
            self.menu.select()
        elif input_key == "back":
            self.menu.up()
        elif input_key == "exit":
            self.menu.clear()

        self.painter.update()

    def track_playback_started(self, tl_track):
        self.painter.update()

    def track_playback_ended(self, tl_track, time_position):
        self.painter.update()
