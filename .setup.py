import sys

assert sys.version_info >= (3, 6), 'fatal: python3.6+ needed to run.'

import io
import contextlib
import shutil
import pathlib
import os

with contextlib.redirect_stdout(io.StringIO()):
    import pygame

if __name__ == "__main__":
    site_packages = f'{pathlib.Path(pygame.__file__).parent.parent.absolute()}'

    if '_8086' in os.listdir(site_packages):
        os.rmdir(os.path.join(site_packages, '_8086'))

    shutil.copytree('_8086', os.path.join(site_packages, '_8086'))
