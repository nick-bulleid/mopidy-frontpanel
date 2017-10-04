from __future__ import unicode_literals

class BrowseMenu:
    def __init__(self, core):
        self.core = core

        self.dir_history = []
        self.dir_current = None
        self.dir_children = []
        self.child_idx = None

    def handle_input(self, input_key):
        if input_key == "left":
            if self.child_idx > len(self.dir_children):
                self.child_idx = 0
            self.child_idx += 1
        elif input_key == "right":
            if self.child_idx == 0:
                self.child_idx = len(self.dir_children)
            self.child_idx -= 1
        elif input_key == "select":
            pass
        elif input_key == "back":
            dir_parent = self.dir_history.pop()
            self.dir_children = self.core.library.browse(dir_parent.uri).get()
            self.child_idx = self.dir_children.index(self.dir_current)
            self.dir_current = dir_parent
        elif input_key == "exit":
            self.dir_history = []
            self.dir_current = None
            self.dir_children = []
            self.child_idx = None
