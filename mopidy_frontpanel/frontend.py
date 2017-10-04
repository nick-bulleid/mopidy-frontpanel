from __future__ import unicode_literals

import logging

from mopidy.core import CoreListener

import pykka

from .menu import BrowseMenu
from .painter import Painter

logger = logging.getLogger(__name__)

class FrontPanel(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(FrontPanel, self).__init__()
        self.core = core
        self.painter = Painter(core, self)
        self.menu = BrowseMenu(core)

    def on_start(self):
        self.painter.start()

    def handleInput(self, input):
        if (input == "play"):
            self.core.playback.resume()
        elif (input == "pause"):
            self.core.playback.pause()
        elif (input == "stop"):
            self.core.playback.stop()
        elif (input == "vol_up"):
            pass
        elif (input == "vol_down"):
            pass
        else:
            self.menu.handleInput(input)

        self.painter.update()

    def track_playback_started(self, tl_track):
        self.painter.update()

    def track_playback_ended(self, tl_track, time_position):
        self.painter.update()
