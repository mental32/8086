# import _8086_crt as crt

from .shell import Shell
from .scenes import Boot
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
        self.layers = []
        self.config = {'os': 'gooper'}

        self.__shell = Shell(self)

        self.update = self._update

    def __repr__(self):
        return f'<[{self.__vmloop_id}] VMLoop object @ 0x{hex(id(self))[2:].upper()}>'

    def __iter__(self):
        if not self.layers:
            self.layers = [Textbox.from_window(self.window)]
            self.__shell._console = self.layers[-1]
            scene = Boot(self.window, {'textbox': self.layers[-1], 'vm': self})
            self.update = scene.start()
        return self

    def __next__(self):
        pass

    def _update(self):
        if self.window.getch():
            self.window.update(self.__shell.react(self.window.key))
