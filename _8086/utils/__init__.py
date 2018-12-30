import sys

assert '_8086' in sys.modules, 'Disallowed: Cannot directly import 8086 submodules.'

from . import colors
from .textbox import Textbox
from .savefile import SaveFile


_debug_counter = 0
def debug(string):
    print(f'[{_debug_counter}] {string}')
    globals()['_debug_counter'] += 1

def __getattribute__(name):
    raise AttributeError('Module attribute access disallowed.')
