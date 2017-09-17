from __future__ import unicode_literals

import logging

from mopidy.core import CoreListener

import pykka

import Adafruit_SSD1306

from PIL import Image, ImageDraw, ImageFont

# Raspberry Pi pin configuration:
RST = 24

logger = logging.getLogger(__name__)

class FrontPanel(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(FrontPanel, self).__init__()
        self.core = core
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

    def on_start(self):
        self.disp.begin()
        self.update()

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
        self.update()

    def track_playback_ended(self, tl_track, time_position):
        self.update()

    def update(self):
        width = self.disp.width
        height = self.disp.height

        image = Image.new('1', (width, height))
        font = ImageFont.load_default()
        draw = ImageDraw.Draw(image)

        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        current_track = self.core.playback.get_current_track().get()
        if current_track is not None:
            draw.text((2, 0), current_track.name, font=font, fill=255)
            draw.text((2, 8), current_track.album.name, font=font, fill=255)
            artists = ', '.join(sorted([a.name for a in current_track.artists]))
            draw.text((2, 16), artists, font=font, fill=255)
        else:
            draw.text((0, 0), "No playing track", font=font, fill=255)

        self.disp.image(image)
        self.disp.display()

