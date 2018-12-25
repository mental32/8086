import sys

assert '_8086' in sys.modules, 'Disallowed: Cannot directly import 8086 submodules.'

from .textbox import Textbox
from .filesystem import Filesystem
from .savefile import SaveFile

def __getattribute__(name):
    raise AttributeError('Module attribute access disallowed.')
