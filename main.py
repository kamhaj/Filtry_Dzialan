'''
...
'''
from task_1.db_creation_actions_filters_1 import DB as DB
#import subprocess
import os

def main():
	## task 1 - create db using data from provided .sql and .csv files
	sql_db = DB()                   # create database instance
	sql_db.run_sql_files()          # create db from provided data (.sql and .csv files)
	sql_db.close_db_connection()    # finish connection do database


	## task 2
    ## TODO 


	## task 3 & task 4
    ## TODO 


	# ## task 5
    ## TODO 
	# #subprocess.run(["pytest", "-v", "-m 'task_1'"])
	# os.system("pytest ../tests/ -v -m task_1")
	# os.system("pytest ../tests/ -v -m task_2")
	# os.system("pytest ../tests/ -v -m task_34")


	## task 6
    ## TODO 

	return 0


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()