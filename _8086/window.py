import time

import pygame

from _8086 import __version__ as _module_version

def debug(string, __c=0):
    print(f'[{__c}] {string}')
    __c += 1

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

    def __iter__(self):
        if type(self.__screen) != pygame.Surface:
            self.__screen = pygame.display.set_mode([self.width, self.height])

            for child in self.children:
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

    def text(self, text, position, colour=None, size=80, font=__font):
        surface = font.render(''.join(chr(c) for c in text), True, colour or (0, 0, 0))
        rect = surface.get_rect()
        rect.topleft = position
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

