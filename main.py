from db_creation.db_creation_actions_filters import DB as DB
import os

def main():
	## task 1 - create db using data from provided .sql and .csv files
	sql_db = DB()                   # create database instance
	sql_db.run_sql_files()          # create db from provided data (.sql and .csv files)
	sql_db.close_db_connection()    # finish connection do database

	return 0


if __name__ == '__main__':
    main()