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

    while window.alive:
        key = window.getch()

        # We may want to communicate with our VMs
        #
        # if key is not None:
        #     with vm.channel.lock():
        #         vm.channel.send(key)

        for _ in vm:
            print(_)


if __name__ == '__main__':
    main()
