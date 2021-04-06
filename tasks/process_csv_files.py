'''

process CSV files:
1. Prepare .sql files with CREATE TABLE statements based on header row
2. Prepare .sql files with INSERT INTO statemenets based on data (row by row)

'''
import pandas as pd
from os.path import isfile, join
import os


csv_files_directory = "../data/csv_files"


## new sql file, INSERT INTO statements with values taken from CSV files (row by row)
## assumption: no data in CSV files missing
def create_insert_into_statements_sql_files():
	# define csv files generator and convert dataframes to SQL tables
	csv_file_gen = get_single_csv_file_generator()

	while True:
			try: 
				current_csv_file = next(csv_file_gen)
			except:
				break

			# prepare SQL table name
			table_name = ((current_csv_file[1]).split('.')[0]).upper()
			table_name = table_name.split('_')[-1]

			# prepare INSERT INTO rows and write to a file
			# insert into car (id, make, model, price) values (1, 'Maserati', 'Quattroporte', '84994.84');
			column_names = current_csv_file[0].columns.to_list()
			get_column_names_without_pk(table_name, column_names)
			
			column_names_str = ','.join(column_names) 
			indices = [list(current_csv_file[0].columns).index(column) for column in column_names]
			
			with open(join(csv_files_directory, f'{table_name}_insert_into.sql'), 'w', encoding='utf-8') as f:
				for index, row in current_csv_file[0].iterrows():
					row_values_list = [current_csv_file[0][label].values[index] for label in column_names]
					row_values_str = ','.join([str(elem) if not isinstance(elem, str) else "'"+str(elem)+"'" for elem in row_values_list])
					insert_statement = f'INSERT INTO {table_name} ({column_names_str}) VALUES ({row_values_str});\n'
					f.write(insert_statement)

	return 0


## generator, easy to modify yielding if CSV file were too large for processing single file at one go
def get_single_csv_file_generator(folder_path=csv_files_directory):
	# get all '.sql' files in a given folder
	csv_files = get_all_files_in_path_with_given_extension(extension='.csv', folder_path=folder_path)

	# exit program if no sql files were found to be run
	if len(csv_files) == 0:
		print("No '.csv' files found under given path.")
		sys.exit()	

	for csv_file in csv_files:
		csv_file_df = pd.read_csv(join(csv_files_directory, csv_file), sep=';')
		yield (csv_file_df , csv_file)
	return 0
    

## get column names (without Primary Key column) from dataframe.columns and table name (PK: ID_<table_name>)
## separate them with commas 
def get_column_names_without_pk(table_name, columns):
	# remove PK (it's autoincremented)
	pk_column = f'ID_{table_name.upper()}'
	columns.remove(pk_column)

	# no need to return columns (passed by reference)
	return 0



## why import from help_functions does not work?? Check it later.
def get_all_files_in_path_with_given_extension(extension, folder_path):
	# get all ".extension" files
	files = [f for f in os.listdir(folder_path) if (isfile(join(folder_path, f)) and f.endswith(extension))]
	return sorted(files)

    
create_insert_into_statements_sql_files()