from __future__ import unicode_literals

class BrowseMenu:
    def __init__(self, core):
        self.core = core

        self.history = []
        self.items = []
        self.idx = 0

    def next():
        if self.idx > len(self.items):
            self.idx = 0
        self.idx += 1

    def prev():
        if self.idx == 0:
            self.idx = len(self.items)
        self.idx -= 1

    def up():
        lastDir = self.history.pop()
        # TODO - handle case of empty history
        self.items = self.core.library.browse(self.history[-1]).get()
        self.idx = self.items.index(lastDir)

    def down():
        pass

    def clear():
        self.history = []
        self.items = []
        self.idx = 0

    def get_name(idx):
        pass

    def get_current_index():
        pass
