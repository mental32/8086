

class TitleScreen:
    def __init__(self, window):
        self.window = window

    def __enter__(self):
        return self

    def __exit__(self, *_):
        pass

    def main(self):
        window = self.window
        screen = window.screen

        screen.fill((0, 0, 0))
        window.text((ord(c) for c in 'Save'), (100, 100), color=(255, 255, 255))
        window.update()

        while True:
            pass
