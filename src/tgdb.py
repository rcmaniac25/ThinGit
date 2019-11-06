import logging
from pathlib import Path

logging = logging.getLogger(__name__) #XXX is this the name we want?

class TGDatabase:
	def __init__(self, path):
		self._path = path
		self._exists = path.exists()
		logging.debug('Created database "%s"', self._path)

	@property
	def path(self):
		return self._path

	@property
	def exists(self):
		return self._exists

	def load(self):
		#TODO
		pass

# XXX Been told to use sqlalchemy as a database abstraction layer