import string

from .scenes import LevelSelector, GameLevel
from .utils import Textbox


def _vmloop_id(__counter=-1):
    __counter += 1
    return __counter


class _8086_VMLOOP:
    '''Root state controller for 8086_GAME.
    Each instance of this can be considered its own seperate game session.
    '''
    __vmloop_id = None

    def __init__(self, window):
        self.__vmloop_id = _vmloop_id()
        self.window = window

    def preload(self):
        self.layers = [LevelSelector(self.window)]

    def __repr__(self):
        return f'<[{self.__vmloop_id}] VMLoop object @ 0x{hex(id(self))[2:].upper()}>'

    def __iter__(self):
        return self

    def __next__(self):
        pass

    @property
    def layer(self):
        return self.layers[-1]

    def update(self):
        if not self.layers:
            return 'KILLME'

        rv = self.layer.update()

        if rv is None:
            return
        elif rv == 'KILLME':
            self.layers.pop()
        else:
            self.layers.append(rv)

        # if self.window.getch():
        #     key = self.window.key

        #     if key == 13 and self.layer.curline:
        #         _string = self.layer.curline
        #         print(repr(_string))

        #     if chr(key) in string.printable:
        #         self.layer.addchar(key)

        #         if key == 13:
        #             self.layer.writestr('>')

        #         self.window.update(self.layer.update())

        #     elif key == 8 and self.layer.curline:
        #         self.layer.buffer = self.layer.buffer[:-1]
        #         self.window.update(self.layer.update())
