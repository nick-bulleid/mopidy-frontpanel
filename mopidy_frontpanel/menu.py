from __future__ import unicode_literals

class BrowseMenu:
    def __init__(self, core):
        self.core = core

        self.dirHistory = []
        self.dirCurrent = None
        self.dirChildren = []
        self.childIdx = None

    def handleInput(self, input):
        if input == "left":
            if (self.childIdx > len(self.dirChildren))
                self.childIdx = 0
            self.childIdx += 1

        elif input == "right":
            if (self.childIdx == 0)
                self.childIdx = len(self.dirChildren)
            self.childIdx -= 1

        elif input == "select":
            pass

        elif input == "back":
            dirParent = self.dirHistory.pop()
            self.dirChildren = self.core.library.browse(dirParent.uri).get()
            self.childIdx = self.dirChildren.index(self.dirCurrent)
            self.dirCurrent = dirParent

        elif input == "exit":
            self.dirCurrent = None
            self.dirHistory = []
            self.refCurrent = None
            self.refList = []
