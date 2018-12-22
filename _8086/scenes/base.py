class BaseScene:
	'''Base class for anything that can be considered a "scene"'''
	def __init__(self, window, metadata):
		self.window = window
		self.metadata = metadata

	def start(self):
		raise NotImplementedError

	def stop(self):
		raise NotImplementedError
