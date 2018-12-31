import itertools
import random
import time

import pygame

def crt_animation(window):
    _w, _h = window.font.size('A')
    partial_width = window.width // 10

    threads = []
    x = 0
    color = itertools.cycle(((255, 0, 0), (0, 255, 0), (0, 0, 255)))

    for thread in range(partial_width):
        threads.append([x, 0, 10, 0, next(color)])
        x += 10

    while threads:
        pygame.event.pump()
        # loop over the threads and advance their position.
        _t = []

        while threads:
            thread = threads.pop()
            x, y, w, h, c = thread

            window.rect(x, y, w, h, color=c)
            h += random.choice((10, 0))

            if h < (window.height + 20):
                _t.append([x, y, w, h, c])

        window.update()
        threads = _t
        time.sleep(0.01)
