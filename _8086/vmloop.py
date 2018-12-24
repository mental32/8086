# import _8086_crt as crt

from .scenes import Textbox, Boot

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

        self.update = self.__update

    def __repr__(self):
        return f'<[{self.__vmloop_id}] VMLoop object @ 0x{hex(id(self))[2:].upper()}>'

    def __iter__(self):
        if not self.layers:
            self.layers = [Textbox.from_window(self.window)]
            self.update = Boot(self.window, {'textbox': self.layers[-1], 'vm': self}).start()
        return self

    def __next__(self):
        pass

    def __update(self):
        pass
