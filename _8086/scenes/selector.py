
from .level import GameLevel


class LevelSelector:
    def __init__(self, window, savefile=None):
        self.window = window
        self.savefile = savefile

        self._max_display = window.width // 70 # Size of a level box + padding
        self.__cursor = 0

        self.__blit()

    def __fill(self):
        self.window.screen.fill((0, 0, 0))

    def __blit(self):
        self.__fill()

        x = _X_BASE = 20
        y = 15
        counter = 0

        self.window.rect(0, 15, 5, 120, (255, 0, 0))
        self.window.rect(0, 155, 5, 190, (0, 255, 0))
        self.window.rect(0, 365, 5, 120, (0, 0, 255))        

        for _ in range(self._max_display * (self.window.height // 70)):
            self.window.rect(x, y, 50, 50, (255, 255, 255))
            self.window.rect(x + 2, y + 2, 46, 46, (50, 50, 50))
            self.window.text(f'{_}', (x + 25, y + 25), (255 ,255, 255), center=True)

            if self.__cursor == _:
                self.window.rect(x - 7, y + 35, 5, 20, (255, 0, 0))
                self.window.rect(x - 7, y + 52, 25, 5, (255, 0, 0))

                self.window.rect(x - 7, y - 7, 5, 20, (255, 0, 0))
                self.window.rect(x - 7, y - 7, 25, 5, (255, 0, 0))

                self.window.rect(x + 52, y - 7, 5, 20, (255, 0, 0))
                self.window.rect(x + 32, y - 7, 25, 5, (255, 0, 0))

                if self.__cursor <= 13:
                    _ZONE_COLOR = (255, 0, 0)
                elif self.__cursor <= 34:
                    _ZONE_COLOR = (0, 255, 0)
                else:
                    _ZONE_COLOR = (0, 0, 255)

                self.window.rect(x + 32, y + 52, 25, 5, _ZONE_COLOR)
                self.window.rect(x + 52, y + 35, 5, 20, _ZONE_COLOR)

            x += 70

            if counter == (self._max_display - 1):
                y += 70
                x = _X_BASE
                counter = 0
            else:
                counter += 1

        self.window.update()

    def update(self):
        if self.window.getch():
            key = self.window.key

            if chr(key) == 'q':
                return 'KILLME'

            elif key == 13:
                pass
                # return GameLevel(self.window, self.savefile.data[self.__cursor])

            elif key == 273 and self.__cursor > (self._max_display - 1):
                self.__cursor -= self._max_display

            elif key == 274 and self.__cursor < (self._max_display * ((self.window.height // 70) - 1)):
                self.__cursor += self._max_display

            elif key == 275 and (self.__cursor % self._max_display) + 1 < self._max_display:
                self.__cursor += 1

            elif key == 276 and (self.__cursor % self._max_display) > 0:
                self.__cursor -= 1

            self.__blit()
