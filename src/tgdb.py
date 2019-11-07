import logging
from pathlib import Path

logging = logging.getLogger(__name__)

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

	def _refresh_exists(self):
		self._exists = self._path.exists()
		return self._exists

	def load(self):
		logging.info('Loading database')
		if not self._refresh_exists():
			logging.error('Database doesn\'t exist "%s", not doing anything', self._path)
			return
		#TODO

	def create_and_load(self):
		logging.info('Creating and loading database')
		if self._refresh_exists():
			logging.info('Database already exists. Moving onto loading')
		else:
			#TODO: create

			#TMP code
			with open(self._path, mode='w') as f:
				print('Hello world', file=f)
		self.load()

# XXX Been told to use sqlalchemy as a database abstraction layer