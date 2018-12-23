import sys

try:
    import _8086
except ImportError:
    sys.path.append('.')
    import _8086

import argparse

def main():
    # TODO: Argparsing
    # TODO: Save files

    # Extract the module components
    VMLoop, Window = _8086.components

    # Instantiate
    vm, window = VMLoop(), Window()

    for _ in window:
        key = window.getch()

if __name__ == '__main__':
    main()
