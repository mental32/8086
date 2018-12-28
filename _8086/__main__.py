import sys

from .prelude import TitleScreen
from .utils import SaveFile

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
            # Title screen (save file manager)
            with TitleScreen(window) as screen:
                save = screen.main()

            vm = VMLoop(window)

            window.children = [vm]

            for _ in window:
                vm.update()

    except KeyboardInterrupt:
        print('\nExiting...')

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument()
    main()
