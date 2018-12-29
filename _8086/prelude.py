import os
import time
import pathlib
import platform
import itertools

from .utils import SaveFile

_save_file_dir = None
_system_type = platform.system().lower()

if _system_type == 'linux':
    _save_file_dir = pathlib.Path.home().absolute() / '._8086'

if not _save_file_dir.exists():
    os.mkdir(f'{_save_file_dir}')

_save_file_dir = f'{_save_file_dir}'

def make_save(username):
    save_path = os.path.join(_save_file_dir, username)
    os.mkdir(save_path)
    return SaveFile(save_path)


class TitleScreen:
    def __init__(self, window):
        self.window = window
        self._index = 0
        self.__state = 0
        self.__inbuf = ''

        self._font_width, self._font_height = window.font.size('A')
        self._files = files = ['New save']

        for item in os.listdir(_save_file_dir):
            if len(item) <= 16 and os.path.isdir(os.path.join(_save_file_dir, item)):
                self._files.append(item)
        else:
            _file_len = len(files) - 1

        self.__handlers = {
            273: lambda: (_file_len)  if (self._index - 1 < 0) else -1,
            274: lambda: (-_file_len) if (self._index == _file_len) else 1,
        }


        width = self.window.width
        height = self.window.height
        _calc = lambda percent: width - (width // percent)
        _wcalc = lambda percent: (width * 2) - (width // percent)

        _, self.__ns_h = self.window.font.size('Username?')
        self.__nsy = ((width // 3) // 2) + (_ // 2)
        self.__nsx = (height // 3) // 2

        self.window.rect(_calc(5), 0, 10, self.window.height, (255, 0, 0))
        self.window.rect(_calc(5) + 10, 0, 10, self.window.height, (0, 255, 0))
        self.window.rect(_calc(5) + 20, 0, 10, self.window.height, (0, 0, 255))
        self.__blit_select()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def __blit_select(self):
        y = self._font_height

        self._fill()
        self.window.text('Select save:', (0, 0), color=(255, 255, 255))

        for i, file in enumerate(self._files):
            string = f'> {file}' if i == self._index else f'- {file}'
            self.window.text(string, (0, y), color=(255, 255, 255))
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
        self.window.text(self.__inbuf, (x + 5, y + (self.__ns_h * 2)), color=(255, 255, 255))

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
                    return make_save(self.__inbuf)

                elif key == 8:
                    if self.__inbuf:
                        self.__inbuf = self.__inbuf[:-1]
                    else:
                        self.__state = 0
                        self._index = 0
                        return self.__blit_select()

                elif chr(key) in 'abcdefghijklmnopqrstuvwxyz' and len(self.__inbuf) < 16:
                    self.__inbuf = self.__inbuf + chr(key)
                    self.__blit_new_save()
