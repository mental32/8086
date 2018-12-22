import sys

assert sys.version_info >= (3, 6), 'fatal: python3.6+ needed to run.'

import io
import contextlib

with contextlib.redirect_stdout(io.StringIO()):
    import pygame

# module specific imports
from .vmloop import _8086_VMLOOP
from .window import _8086_Window

__author__ = 'mental'
__version__ = _8086_Window.__version__

__debug = False

components = (
    _8086_VMLOOP,
    _8086_Window,
)

def __getattribute__(name):
    if name == 'components':
        return components

    raise AttributeError('Module attribute access disallowed.')
