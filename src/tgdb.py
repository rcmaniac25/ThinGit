import logging
from pathlib import Path

from sqlalchemy import create_engine

import tgdb_elements

logging = logging.getLogger(__name__)

class TGDatabase:
	def __init__(self, path):
		self._path = path
		self._exists = path.exists()
		self._loaded = False
		self._engine = None

		logging.debug('Created database "%s"', self._path)

	@property
	def path(self):
		return self._path

	@property
	def exists(self):
		return self._exists

	@property
	def loaded(self):
		return self._loaded

	def _refresh_exists(self):
		self._exists = self._path.exists()
		return self._exists

	def load(self):
		if self._loaded: return
		logging.info('Loading database')
		if not self._refresh_exists():
			logging.error('Database doesn\'t exist "%s", not doing anything', self._path)
			return

		try:
			#XXX might only work if paths are on the same drive (Windows)
			relativePath = self._path.relative_to(Path.cwd())
			logging.debug(relativePath)
			self._engine = create_engine('sqlite:///{0}'.format(relativePath), echo=True)
		except Exception as e:
			logging.exception(e)
			return

		tgdb_elements.metadata_create(self._engine)

		self._loaded = True
		#TODO

	def create_and_load(self):
		if self._loaded: return
		logging.info('Creating and loading database')
		if self._refresh_exists():
			logging.info('Database already exists. Moving onto loading')
		else:
			# sqlalchemy will create the DB if it doesn't exist
			with open(self._path, mode='w') as f:
				logging.debug('Created DB file which will be populated by sqlalchemy: "%s"', self._path)
		self.load()
