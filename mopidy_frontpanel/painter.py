from __future__ import unicode_literals

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306

class Painter:
    def __init__(self, core, menu):
        self.core = core
        self.menu = menu

        serial = spi(spi=spidev, gpio=RPi.GPIO, gpio_DC=24, gpio_RST=25)
        self.device = ssd1306(serial)

    def update(self):
        with canvas(self.device) as draw:
            # draw a black rectangle
            draw.rectangle(self.device.bounding_box, outline=0, fill=0)

            menu_idx = self.menu.get_current_index()
            if menu_idx is not None:
                # draw the menu
                draw.text((0, 0), self.menu.get_name(menu_idx), font=font, fill=255)
                draw.text((0, 8), self.menu.get_type(menu_idx), font=font, fill=255)
                draw.text((0, 16), str(menu_idx + 1) + "/" + str(self.menu.get_count()), font=font, fill=255)
                return

            # otherwise print out the current track
            current_track = self.core.playback.get_current_track().get()
            if current_track is not None:
                draw.text((2, 0), current_track.name, font=font, fill=255)
                draw.text((2, 8), current_track.album.name, font=font, fill=255)
                artists = ', '.join(sorted([a.name for a in current_track.artists]))
                draw.text((2, 16), artists, font=font, fill=255)
            else:
                draw.text((0, 0), "No playing track", font=font, fill=255)

    def print_text(self, text):
        with canvas(self.device) as draw:
            # draw a black rectangle
            draw.rectangle(self.device.bounding_box, outline=0, fill=0)

            # draw text
            draw.text((0, 0), text, font=font, fill=255)
