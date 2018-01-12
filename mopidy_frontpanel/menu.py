from __future__ import unicode_literals

class BrowseMenu:
    def __init__(self, core):
        self.core = core

        self.history = []
        self.items = []
        self.idx = None

    def next(self):
        if self.idx is not None:
            if self.idx == len(self.items):
                self.idx = 0
            self.idx += 1

    def prev(self):
        if self.idx is not None:
            if self.idx == 0:
                self.idx = len(self.items)
            self.idx -= 1

    def up(self):
        if len(self.history) == 0:
            self.clear()
        else:
            lastDir = self.history.pop()
            self.items = self.core.library.browse(self.history[-1].url).get()
            self.idx = self.items.index(lastDir)

    def select(self):
        if self.idx == None:
            self.items = self.core.library.browse(None).get()
            self.idx = 0

    def clear(self):
        self.history = []
        self.items = []
        self.idx = None

    def get_name(self, idx):
        if len(self.items) != 0:
            return self.items[idx].name

    def get_current_index(self):
        return self.idx
