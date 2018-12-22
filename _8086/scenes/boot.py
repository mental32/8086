from .base import BaseScene

from _8086 import Textbox

class BootBare(BootBare):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.textbox = Textbox.from_window(self.window)

    def start(self):
        self.textbox.write('A')
        yield 1
        self.textbox.write('B')
        yield 1
        self.textbox.write('C')
        yield 1
        self.textbox.write('D')
        yield 1
