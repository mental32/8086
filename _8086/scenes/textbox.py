import array

class Textbox:
    def __init__(self, window, x, y width, height):
        self.screen = window.screen

        self.width = width
        self.height = height
        self.buffer = array.array('H')

        self.text = lambda s, x, y, c: return window.text(string, (x, y), c or self.color, self.size)

    @classmethod
    def from_window(cls, window):
        return cls(window, 0, 0, window.width, window.height)

    def write(self):
        pass

    def writeln(self, *args, **kwargs):
        self.write(*args, '\n', **kwargs)

    def update(self):
        self.screen.fill(self.bg)

        buffer = self.buffer
        sp = s = y = 0

        slice = buffer[s:]

        while slice.count(NEWLINE):
            s += self.text(buffer[s:slice.index(NEWLINE)].tostring(), 0, y, self.color)
            slice = buffer[s:]
            y += 1

        pygame.display.update(self.screen.get_rect())
