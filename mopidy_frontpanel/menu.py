from __future__ import unicode_literals

from mopidy.models import Ref

class MenuSlice:
    def __init__(self, items)
        self.items = items
        self.idx = 0

    def next(self):
        self.idx += 1
        if self.idx == len(self.items):
            self.idx = 0

    def prev(self):
        self.idx -= 1
        if self.idx < 0:
            self.idx = (len(self.items) - 1)

    def count(self):
        return len(self.items)

    def current_index(self):
        return self.idx

    def get_name(self, idx):
        if idx < len(self.items)
            return self.items[idx].name

    def get_type(self, idx):
        if idx < len(self.items)
            return self.items[idx].type

    def get_current_item(self):
        return self.items[self.idx]

class MenuModel:
    def __init__(self, core):
        self.core = core

        self.history = []
        self.slice = None

    def up(self):
        if len(self.history) == 0:
            self.clear()
        else:
            self.slice = self.history.pop()

    def select(self):
        if self.slice is None:
            self.slice = MenuSlice(self.core.library.browse(None).get())
        else:
            item = self.slice.get_current_item()
            if item.type is Ref.TRACK:
                pass
            else:
                self.history.append(self.slice)
                self.slice = MenuSlice(self.core.library.browse(item.uri).get())

    def clear(self):
        self.history = []
        self.slice = None

    def next(self):
        if self.slice is not None:
            self.slice.next()

    def prev(self):
        if self.slice is not None:
            self.slice.prev()

    def get_name(self, idx):
        if self.slice is not None:
            return self.slice.name(idx)

    def get_type(self, idx):
        if self.slice is not None:
            return self.slice.type(idx)

    def get_count(self):
        if self.slice is not None:
            return self.slice.count()
        else:
            return 0

    def get_current_index(self):
        if self.slice is not None:
            return self.slice.current_index()
