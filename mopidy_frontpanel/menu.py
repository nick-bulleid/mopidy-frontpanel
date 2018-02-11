from __future__ import unicode_literals

from mopidy.models import Ref

class BrowseMenu:
    def __init__(self, core):
        self.core = core

        self.history = []
        self.items = []
        self.idx = None

    def next(self):
        if self.idx is not None:
            self.idx += 1
            if self.idx == len(self.items):
                self.idx = 0

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
            uri = None
            if len(self.history) != 0:
                uri = self.history[-1].uri

            self.items = self.core.library.browse(uri).get()
            self.idx = self.items.index(lastDir)

    def select(self):
        if self.idx is not None:
            item = self.items[self.idx]
            if item.type is Ref.TRACK:
                pass
            else:
                self.history.append(item)
                self.items = self.core.library.browse(item.uri).get()
                self.idx = 0
        else:
            self.items = self.core.library.browse(None).get()
            self.idx = 0

    def clear(self):
        self.history = []
        self.items = []
        self.idx = None

    def get_name(self, idx):
        if len(self.items) == 0:
            return "Empty"
        elif len(self.items) > idx:
            return self.items[idx].name

    def get_type(self, idx):
        if len(self.items) > idx:
            return self.items[idx].type

    def get_count(self):
        return len(self.items)

    def get_current_index(self):
        return self.idx
