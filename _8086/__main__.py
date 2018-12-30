import sys

from .prelude import TitleScreen
from . import scenes

try:
    import _8086
except ImportError:
    sys.path.append('.')
    import _8086

import argparse

def main():
    # Extract the module components
    VMLoop, Window = _8086.components

    try:

        with Window() as window:
            screen = TitleScreen(window)

            for _ in window:
                _savefile = screen.update()
                if _savefile:
                    window.blank()
                    scenes.crt_animation(window)
                    break

            window.blank()
            vm = VMLoop(window)

            window.children = [vm]

            for _ in window:
                vm.update()

    except KeyboardInterrupt:
        print('\nExiting...')

if __name__ == '__main__':
    main()
