from pathlib import Path

class TGDatabase:
	def __init__(self, path):
		self._path = path
		self._exists = path.exists()

	@property
	def path(self):
		return self._path

	@property
	def exists(self):
		return self._exists

	def load(self):
		pass

# XXX Been told to use sqlalchemy as a database abstraction layer