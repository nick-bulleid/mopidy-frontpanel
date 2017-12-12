from __future__ import unicode_literals

from gpiozero import Button

class Input:
    def __init__(self, controller):
        self.controller = controller

        left_pin = Button(21)
        right_pin = Button(22)
        knob_pin = Button(17)
        back_pin = Button(18)

        left_pin.when_pressed = on_left_turn
        right_pin.when_pressed = on_right_turn
        knob_pin.when_pressed = on_knob_press
        back_pin.when_pressed = on_back_press

    def on_left_turn(self):
        self.controller.handle_input("prev")

    def on_right_turn(self):
        self.controller.handle_input("next")

    def on_knob_press(self):
        self.controller.handle_input("select")

    def on_back_press(self):
        self.controller.handle_input("back")
