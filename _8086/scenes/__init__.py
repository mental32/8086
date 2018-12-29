import sys

assert '_8086' in sys.modules, 'Disallowed: Cannot directly import 8086 submodules.'

from .boot import Boot
from .crt import crt_animation

def __getattribute__(name):
    raise AttributeError('Module attribute access disallowed.')
