'''
Przygotuj skrypt, który na podstawie wskazanych plików .csv oraz .sql 
(lista i opis plików znajduje się pod zadaniami)utworzy bazę sqlite3. 
W razie potrzeby dodaj brakujące więzy integralnościi/lub inne 
elementy/struktury.
'''

import sqlite3 as sql
import os
import sys
from help_functions import get_all_files_in_path_with_given_extension


## define paths for given data files
sql_files_directory = "../data/sql_files"

## database file path
db_file_path = '../company_database.db'


class DB():
	def __init__(self):
		print("DB object creation...")
		try:
			# connect to a database (file) and create cursor
			self.connection  = sql.connect(db_file_path)
			self.cursor = self.connection.cursor()
		except Exception as e:
			print('Exception: {}'.format(e))
			raise Exception(e)


	def close_db_connection(self):
		print("Closing database connection...")
		self.connection.commit()
		self.connection.close()

	## getter
	def get_connection(self):
		return self.connection

	## create Actions Filter structure (empty FTD and FTD_elementy tables) in database 
	def run_ftd_sql_files(self):
		# define sql files generator and run sql commands, break if impossible (no more files)
		sql_file_as_string_gen = self.get_single_sql_file_as_string_generator()
		while True:
			try: 
				self.cursor.executescript(next(sql_file_as_string_gen))	
			except Exception as e:
				print('No more .sql files to process')
				break

		return 0


	## generator function for converting files to strings (one by one)
	def get_single_sql_file_as_string_generator(self, folder_path=sql_files_directory):
		# get all '.sql' files in a given folder
		sql_files = get_all_files_in_path_with_given_extension(extension='.sql', folder_path=folder_path)
		print("SQL FILES:")
		print(sql_files)
		# exit program if no sql files were found to be run
		if len(sql_files) == 0:
			print("No '.sql' files found under given path")
			sys.exit()

		# run all ".sql" files in a given folder (e.g. CREATE TABLES statements)
		# order may matter...(tables dependencies). It's a good idea to put dependant statements in a correct order
		for sql_file in sql_files:
			print(f'Processing {sql_file} file...')
			sql_file_as_str = open(os.path.join(folder_path, sql_file), encoding='utf-8').read()
			yield sql_file_as_str

		return 0



