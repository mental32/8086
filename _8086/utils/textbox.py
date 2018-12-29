import array

import pygame

NEWLINE = 13


class Textbox:
    def __init__(self, window, x, y, width, height, cursor=True, size=20, font=None, bg=(0, 0, 0), fg=(255, 255, 255)):
        self.screen = window.screen

        self.font = font or window.font

        self.width = width
        self.height = height
        self.buffer = array.array('H')

        self.bg, self.fg = bg, fg
        self.size = size

        self.cursor = cursor

        self._rect = window.rect

        self.text = lambda s, x, y, c=None: window.text(s, (x, y), c or fg, size)

    @classmethod
    def from_window(cls, window):
        return cls(window, 0, 0, window.width, window.height)

    @property
    def curline(self):
        arr = []
        c = 1

        for byte in self.buffer[::-1]:
            if byte == 13:
                break

            elif byte:
                arr.append(self.buffer[-c])
                c += 1

        return ''.join(chr(c) for c in arr[:-1])[::-1]

    def addchar(self, key):
        self.buffer.append(key)

    def drain(self):
        self.buffer = array.array('H')

    def write(self, string):
        self.buffer.extend(array.array('H', string if hasattr(string, '__iter__') else (string,)))
        return self

    def writestr(self, string):
        self.write((ord(c) for c in string))
        return self

    def writeln(self, string):
        self.writestr(string)
        self.buffer.append(NEWLINE)
        return self

    def update(self):
        self.screen.fill(self.bg)

        y = 0

        buffer = self.buffer.tobytes()[:-1].split(b'\x0d')

        if len(buffer) > (self.height // self.size):
            slice = buffer[len(buffer) - (self.height // self.size):]
        else:
            slice = buffer

        for line in slice:
            lt = tuple(b for b in line if b)

            _w, _ = self.font.size(''.join(chr(c) for c in lt))

            self.text(lt, 0, y * self.size)
            y += 1

        if self.cursor:
            w, h = self.font.size(' ')
            self._rect(_w, (y - 1) * self.size, w, h, self.fg, screen=self.screen)

        return self.screen.get_rect()
