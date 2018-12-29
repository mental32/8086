import sys

assert '_8086' in sys.modules, 'Disallowed: Cannot directly import 8086 submodules.'

from .textbox import Textbox
from .savefile import SaveFile

def debug(string, __c=0):
    print(f'[{__c}] {string}')
    __c += 1

def __getattribute__(name):
    raise AttributeError('Module attribute access disallowed.')
