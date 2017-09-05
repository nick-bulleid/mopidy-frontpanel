from __future__ import unicode_literals

import logging

from mopidy.core import CoreListener

import pykka


logger = logging.getLogger(__name__)

class FrontPanel(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(FrontPanel, self).__init__()
        self.core = core

    def onPlayPause(self):
        pass

    def onNext(self):
        pass
    
    def onPrev(self):
        pass

    def onStop(self):
        pass

    def onMenu(self):
        pass

    def onLeftTurn(self):
        pass

    def onRightTurn(self):
        pass

    def onBack(self):
        pass

    def track_playback_started(self, tl_track):
        pass

    def track_playback_ended(self, tl_track, time_position):
        pass
