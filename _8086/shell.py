import array
import shlex
import string


class Shell:
    def __init__(self, vm):
        self.vm = vm
        self.__buffer = array.array('H')

    @property
    def console(self):
        return self._console

    def react(self, key):
        print(key)

        if key == 13 and self.__buffer:
            self.exec(''.join(chr(c) for c in self.__buffer.tolist()))
            self.__buffer = array.array('H')
            return self._console.write(13).writestr('? ').update()

        elif key == 8:
            if self.__buffer and self.__buffer[-1] != 13:
                self._console.buffer.pop()
                self.__buffer.pop()

            return self._console.update()

        elif chr(key) in string.printable:
            self.__buffer.append(key)
            return self._console.write(key).update()

    def exec(self, string):
        splitted = shlex.split(string)
        print(splitted)
