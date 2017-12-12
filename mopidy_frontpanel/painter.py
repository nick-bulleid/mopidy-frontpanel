from __future__ import unicode_literals

import Adafruit_SSD1306 # pylint: disable=import-error

from PIL import Image, ImageDraw, ImageFont # pylint: disable=import-error

# Raspberry Pi pin configuration:
RST = 24

class Painter:
    def __init__(self, core, menu):
        self.core = core
        self.menu = menu
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

    def start(self):
        self.disp.begin()
        self.update()

    def update(self):
        # get screen size
        width = self.disp.width
        height = self.disp.height

        # create a drawing surface
        image = Image.new('1', (width, height))
        font = ImageFont.load_default()
        draw = ImageDraw.Draw(image)

        # draw a black rectangle
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # print out the current track
        current_track = self.core.playback.get_current_track().get()
        if current_track is not None:
            draw.text((2, 0), current_track.name, font=font, fill=255)
            draw.text((2, 8), current_track.album.name, font=font, fill=255)
            artists = ', '.join(sorted([a.name for a in current_track.artists]))
            draw.text((2, 16), artists, font=font, fill=255)
        else:
            draw.text((0, 0), "No playing track", font=font, fill=255)

        # send image to screen
        self.disp.image(image)
        self.disp.display()

    def print_text(self, text)
        # get screen size
        width = self.disp.width
        height = self.disp.height

        # create a drawing surface
        image = Image.new('1', (width, height))
        font = ImageFont.load_default()
        draw = ImageDraw.Draw(image)

        # draw a black rectangle
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # draw text
        draw.text((0, 0), text, font=font, fill=255)

        # send image to screen
        self.disp.image(image)
        self.disp.display()
