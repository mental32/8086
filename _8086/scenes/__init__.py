import sys

assert '_8086' in sys.modules, 'Disallowed: Cannot directly import 8086 submodules.'

from .crt import crt_animation
from .selector import LevelSelector
from .level import GameLevel

def __getattribute__(name):
    raise AttributeError('Module attribute access disallowed.')
