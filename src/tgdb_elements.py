from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Model(Base):
	__tablename__ = 'models'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	path = Column(String)

	def __init__(self, path):
		self.name = path.name
		self.path = str(path)

	def __repr__(self):
		return 'Model({0}, {1})'.format(self.name, self.path)

#TODO

def metadata_create(engine):
	Base.metadata.create_all(engine)
