import sys

assert '_8086' in sys.modules, 'Disallowed: Cannot directly import 8086 submodules.'

# Imports
from .textbox import Textbox
from .filesystem import Filesystem

def __getattribute__(name):
    raise AttributeError('Module attribute access disallowed.')
