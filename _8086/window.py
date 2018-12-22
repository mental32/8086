import pygame


class _8086_Window:
    pygame.init()

    __version__ = '0.0.1a'

    def __init__(self):
        self.__key_buffer = None
        self.__key_lock = 0

        self.__screen = None
        self._width = 500
        self._height = 500

    def __iter__(self):
        if type(self.__screen) != pygame.Surface:
            self.__screen = pygame.display.set_mode([self.width, self.height])
        return self

    def __next__(self):
        pass

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

    def text(self, text, position, colour=None, size=80):
        surface = pygame.font.SysFont('firacode', size).render(''.join(chr(c) for c in text), True, colour or (0, 0, 0))
        rect = surface.get_rect()
        rect.topleft = position
        self.__screen.blit(surface, rect)
        return len(text)

    def getch(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.__key_lock = 0
                self.__key_buffer = event.key

            elif event.type == pygame.KEYUP:
                self.__key_buffer = None

        if not self.__key_lock:
            self.__key_lock = 1
            return self.__key_buffer
        else:
            return None
