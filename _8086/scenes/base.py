class BaseScene:
    '''Base class for anything that can be considered a "scene"'''
    def __init__(self, window, metadata={}):
        self.window = window

        for k, v in metadata.items():
            setattr(self, k, v)

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError
