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
    window = Window()
    vm = VMLoop(window)

    window.children = [vm]

    try:
        for _ in window:
            vm.update()
    except KeyboardInterrupt:
        print('\nExiting...')

if __name__ == '__main__':
    main()
