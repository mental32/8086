import array

import pygame

NEWLINE = 13


class Textbox:
    def __init__(self, window, x, y, width, height):
        self.screen = window.screen

        self.width = width
        self.height = height
        self.buffer = array.array('H')

        self.color = (0, 255, 0)
        self.bg = (0, 0, 0)
        self.size = 20

        self.text = lambda s, x, y, c=None: window.text(s, (x, y), c or self.color, self.size)

    @classmethod
    def from_window(cls, window):
        return cls(window, 0, 0, window.width, window.height)

    def write(self, *data):
        self.buffer.extend(array.array('H', (key for key in data)))

    def writeln(self, *args):
        self.write(*args, '\n')

    def update(self):
        self.screen.fill(self.bg)

        y = 0
        buffer = self.buffer.tobytes()[:-1].split(b'\x0d')

        for line in buffer:
            self.text(list(b for b in line if b), 0, y * self.size)
            y += 1

        pygame.display.update(self.screen.get_rect())
