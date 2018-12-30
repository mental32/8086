import sys
import os


class SaveFile:
	def __init__(self, fp):
		self.fp = fp

	def __repr__(self):
		return f'<SaveFile: fp={self.fp!r}>'

	def __bool__(self):
		return bool(self.fp)

	def read(self):
		pass

	def write(self):
		pass
