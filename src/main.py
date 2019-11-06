import logging
import os
import argparse
from pathlib import Path

from tgdb import TGDatabase

supported_src_ext = ['.stl', '.3mf', '.obj', '.amf', '.mix', '.scad']
supported_arc_ext = ['.zip', '.7z', '.rar']
supported_dst_ext = ['.gcode', '.msf']
supported_ext = supported_src_ext + supported_dst_ext + supported_arc_ext

def create_parser():
	parser = argparse.ArgumentParser(description='ThinGit: Personal 3D Model Repository')
	parser.add_argument('-dat', '--datadir', dest='datadir', help='Directory path for database and logging. Overrides --dbpath and --logpath path, but will use the filename set')
	parser.add_argument('-db', '--dbpath', '--database', dest='dbpath', help='Path for database. By default it\'s put in the current working directory when ThinGit is run')
	parser.add_argument('-log', '--logpath', dest='logpath', help='Path for logging. By default, logging is done to stdout/stderr. Setting this variable will enable logging to a file')
	parser.add_argument('-s', '--silent', action='store_true', help='Don\'t produce user prompts. Could mean the ThinGit exits early')
	parser.add_argument('-V', '--verbose', action='store_true', help='Log everything')
	return parser

def preprocess_arguments(args):
	def create_directory_paths(path):
		print(path)
		path.mkdir(parents=True, exist_ok=True)
		
	nargs = argparse.Namespace()

	setattr(nargs, 'datadir', args.datadir)
	setattr(nargs, 'dbpath', args.dbpath)
	setattr(nargs, 'logpath', args.logpath)
	setattr(nargs, 'silent', args.silent)
	setattr(nargs, 'verbose', args.verbose)

	if args.datadir:
		# We will have a data directory, we want database and logging to be stored in it
		d = Path(args.datadir)
		if d.is_file():
			d = d.parent

		create_directory_paths(d.resolve())

		db = d.joinpath('db.dat')
		log = d.joinpath('output.log')

		if args.dbpath:
			db = d.joinpath(os.path.basename(args.dbpath))
		if args.logpath:
			log = d.joinpath(os.path.basename(args.logpath))

		if db == log:
			# Add another .log to make it different
			log.name += '.log'

		setattr(nargs, 'dbpath', str(db))
		setattr(nargs, 'logpath', str(log))
	else:
		if args.dbpath:
			create_directory_paths(Path(args.dbpath).resolve())
		if args.logpath:
			create_directory_paths(Path(args.logpath).resolve())

	return nargs

if __name__ == '__main__':
	parser = create_parser()
	args = preprocess_arguments(parser.parse_args())

	if args.logpath or args.verbose:
		logArgs = {}
		if args.logpath:
			logArgs['filename'] = args.logpath
		if args.verbose:
			logArgs['level'] = logging.DEBUG
		#TODO: change format to log timestamp as well. Useful when logging to file
		logging.basicConfig(**logArgs)

	if args.dbpath:
		db_path = Path(args.dbpath)
	else:
		db_path = Path('.').joinpath('tgdb.dat')
	logging.debug('Creating database at "%s"', db_path)
	db = TGDatabase(db_path.resolve())

	#TODO: log loading DB
	db.load()

	if not db.exists:
		logging.warning('Database file doesn\'t exist')
		print('Missing database...') #DEV: ask if one should be created: https://docs.python.org/3/library/functions.html#input
	#TODO...

	#Test code for walking folders and only checking what we're interested in
	for (dirpath,dirnames,filenames) in os.walk('.'):
		d = Path(dirpath)
		for file in filenames:
			filepath = d.joinpath(file).resolve()
			if filepath.suffix.lower() in supported_ext:
				print(filepath)

# Process
# 1. Look for DB (argument), if none exists, ask if they want to create a DB (put next to executable for now)
# 2. Use config table of DB to figure out where models are stored and where gcode would be...
# 3. ??
