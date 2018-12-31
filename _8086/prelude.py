import os

from .utils.savefile import SaveFile, _save_file_dir


class TitleScreen:
    def __init__(self, window):
        self.window = window
        self._files = files = ['New save']

        for item in os.listdir(_save_file_dir):
            path = os.path.join(_save_file_dir, item)
            if len(item) <= 16 and os.path.isdir(path):
                if 'save.dat' in os.listdir(path):
                    self._files.append(item)
        else:
            _file_len = len(files) - 1

        self.__handlers = {
            273: lambda: (_file_len)  if (self._index - 1 < 0) else -1,
            274: lambda: (-_file_len) if (self._index == _file_len) else 1,
        }

    def preload(self):
        self._index = 0
        self.__state = 0
        self.__inbuf = ''

        self._font_width, self._font_height = self.window.font.size('A')

        width = self.window.width
        height = self.window.height
        _calc = width - (width // 5)

        _, self.__ns_h = self.window.font.size('Username?')
        self.__nsy = ((width // 3) // 2) + (_ // 2)
        self.__nsx = (height // 3) // 2

        self.window.rect(_calc, 0, 10, height, (255, 0, 0))
        self.window.rect(_calc + 10, 0, 10, height, (0, 255, 0))
        self.window.rect(_calc + 20, 0, 10, height, (0, 0, 255))
        self.__blit_select()

    def __blit_select(self):
        y = self._font_height

        self._fill()
        self.window.text('Select save:', (0, 0), color=(255, 255, 255))

        for i, file in enumerate(self._files):
            string = f'> {file}' if i == self._index else f'- {file}'
            self.window.text(string, (0, y), color=((0, 255, 0) if i == self._index else (255, 255, 255)))
            y += self._font_height

        self.window.update()

    def __blit_new_save(self):
        self._fill()

        x = self.__nsx
        y = self.__nsy
        fw = self._font_width

        self.window.text('Username?', (x, y), color=(255, 255, 255))

        self.window.rect(x, y + self.__ns_h, fw * 17, self._font_height * 2, (255, 255, 255))
        self.window.rect(x + 3, y + self.__ns_h + 3, (fw * 17) - 6, (self._font_height * 2) - 6, (0, 0, 0))
        self.window.text(self.__inbuf, (x + 5, y + (self.__ns_h * 2) - 5), color=(255, 255, 255))

        self.window.update()

    def _fill(self):
        self.window.rect(0, 0, (self.window.width // 3) * 2, self.window.height, (0, 0, 0))

    def update(self):
        if self.window.getch():
            key = self.window.key
            state = self.__state

            if state == 0:
                if key == 13:
                    if self._index == 0:
                        self.__state = 1
                        self.__blit_new_save()
                    else:
                        return SaveFile(os.path.join(_save_file_dir, self._files[self._index]))

                elif key in self.__handlers:
                    self._index += self.__handlers[key]()
                    self.__blit_select()

            elif state == 1:
                if key == 13 and self.__inbuf:
                    return SaveFile.new_save(self.__inbuf)

                elif key == 8:
                    if self.__inbuf:
                        self.__inbuf = self.__inbuf[:-1]
                        self.__blit_new_save()
                    else:
                        self.__state = 0
                        self._index = 0
                        return self.__blit_select()

                elif chr(key) in 'abcdefghijklmnopqrstuvwxyz' and len(self.__inbuf) < 16:
                    self.__inbuf = self.__inbuf + chr(key)
                    self.__blit_new_save()
