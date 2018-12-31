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
            vmloop = VMLoop(window)

            while True:
                screen.preload()

                for _ in window:
                    _savefile = screen.update()
                    if _savefile:
                        scenes.crt_animation(window)
                        break

                window.blank()
                window.children = [vmloop]

                vmloop.preload(_savefile)

                for _ in window:
                    if vmloop.update() == 'KILLME':
                        window.blank()
                        break

    except KeyboardInterrupt:
        print('\nExiting...')

if __name__ == '__main__':
    main()
