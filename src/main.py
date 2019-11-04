import os
import argparse
from pathlib import Path

from tgdb import TGDatabase

supported_src_ext = ['.rar', '.scad', '.obj', '.mix', '.stl', '.zip', '.3mf']
supported_dst_ext = ['.gcode', '.msf']
supported_ext = supported_src_ext + supported_dst_ext

def create_parser():
	parser = argparse.ArgumentParser(description='ThinGit: Personal 3D Model Repository')
	parser.add_argument('-db', '--dbpath', '--database', dest='dbpath', help='Path for database. By default it\'s put in the current working directory when ThinGit is run')
	return parser

if __name__ == '__main__':
	parser = create_parser()
	args = parser.parse_args()

	#TODO: setup logging

	if args.dbpath:
		db_path = Path(args.dbpath)
	else:
		db_path = Path('.').joinpath('tgdb.dat')
	db = TGDatabase(db_path.resolve())

	#TODO: log loading DB
	db.load()

	if not db.exists:
		print('Missing database...') #DEV: ask if one should be created
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
