import time
import string

import pygame

from .base import BaseScene
from .textbox import Textbox

class Boot(BaseScene):
    def start(self):
        vm = self.vm
        script = getattr(self, f'_boot_{vm.config["os"].lower()}')()
        update = lambda: pygame.display.update(self.textbox.update())

        def _wrapper():
            try:
                delay = next(script)
                update()
            except StopIteration:
                vm.update = lambda: None
                update()
            else:
                time.sleep(delay)

        return _wrapper

    def _boot_gooper(self):
        vm, console = self.vm, self.textbox
