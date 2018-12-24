import array

import pygame

NEWLINE = 13


class Textbox:
    def __init__(self, window, x, y, width, height, size=20, bg=(0, 0, 0), fg=(255, 255, 255)):
        self.screen = window.screen

        self.width = width
        self.height = height
        self.buffer = array.array('H')

        self.bg, self.fg = bg, fg
        self.size = size

        self.text = lambda s, x, y, c=None: window.text(s, (x, y), c or fg, size)

    @classmethod
    def from_window(cls, window):
        return cls(window, 0, 0, window.width, window.height)

    def drain(self):
        self.buffer = array.array('H')

    def write(self, string):
        self.buffer.extend(array.array('H', string if hasattr(string, '__iter__') else (string,)))

    def writestr(self, string):
        self.write((ord(c) for c in string))

    def writeln(self, string):
        self.writestr(string)
        self.buffer.append(NEWLINE)

    def update(self):
        self.screen.fill(self.bg)

        y = 0

        buffer = self.buffer.tobytes()[:-1].split(b'\x0d')

        if len(buffer) > (self.height // self.size):
            slice = buffer[len(buffer) - (self.height // self.size):]
        else:
            slice = buffer

        for line in slice:
            self.text(list(b for b in line if b), 0, y * self.size)
            y += 1

        return self.screen.get_rect()
