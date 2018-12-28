import sys

assert '_8086' in sys.modules, 'Disallowed: Cannot directly import 8086 submodules.'

from .title import TitleScreen

def __getattribute__(name):
    raise AttributeError('Module attribute access disallowed.')
