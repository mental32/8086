import time

import pygame

from _8086 import __version__ as _module_version
from .utils import debug


class _8086_Window:
    '''Class to provide and internal interface to pygame.'''
    pygame.init()

    try:
        __font = pygame.font.SysFont('firacode', 20)
    except Exception:
        __font = pygame.font.Font('freesans.ttf', 20)

    __version__ = _module_version

    def __init__(self):
        self.__key_buffer = None
        self.__key_lock = 0

        self.__screen = None
        self._width = 500
        self._height = 500

        self.children = []

    def __enter__(self):
        if type(self.__screen) != pygame.Surface:
            self.__screen = pygame.display.set_mode([self.width, self.height])
        return self        

    def __exit__(self, *args):
        pass

    def __iter__(self):
        while self.children:
            child = self.children.pop()
            debug(f'Loaded child {iter(child)}')

        return self

    def __next__(self):
        time.sleep(1 / 60)

    @property
    def key(self):
        return self.__key_buffer

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def screen(self):
        return self.__screen

    @property
    def font(self):
        return self.__font    

    def blank(self):
        self.screen.fill((0, 0, 0))
        self.update()

    def update(self, *args, **kwargs):
        pygame.display.update(*args, **kwargs)

    def rect(self, x, y, w, h, color, screen=None):
        pygame.draw.rect(screen or self.__screen, color, (x, y, w, h))

    def text(self, text, position, color=None, size=80, font=__font, center=False):
        if not isinstance(text, str):
            data = ''.join(chr(c) for c in text)
        else:
            data = text

        surface = font.render(data, True, color or (0, 0, 0))
        rect = surface.get_rect()

        if not center:
            rect.topleft = position
        else:
            rect.center = position

        self.__screen.blit(surface, rect)

    def getch(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.__key_lock = 0
                self.__key_buffer = event.key

            elif event.type == pygame.KEYUP:
                self.__key_buffer = None

        if self.__key_lock:
            return None

        self.__key_lock = 1
        return self.__key_buffer

