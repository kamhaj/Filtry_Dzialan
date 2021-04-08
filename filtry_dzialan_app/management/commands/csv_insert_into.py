'''
create custom commands (python manage.py my_command) 
to run a standalone script (e.g. insert_into_django_db.py) in Django environment
'''


from django.core.management.base import BaseCommand
from filtry_dzialan_app.models import Program, Os, Dzialanie
import pandas as pd
import os

csv_files_directory = 'data/csv_files'



## custom command for inserting CSV data into existing django models (db tables)
class Command(BaseCommand):

	def handle(self, *args, **options):
		self.insert_into_program_table()
		self.insert_into_os_table()
		self.insert_into_dzialanie_table()


	def insert_into_program_table(self, csv_file = '1_program.csv'):
				# read csv file
		df =  pd.read_csv(os.path.join(csv_files_directory, csv_file), sep=';')

		# iterate through dataframe and add rows to database
		for index, row in df.iterrows():
			# get a list of values stored in a row
			row_values_list = [df[label].values[index] for label in df.columns.to_list()]

			# get incides of df columns needed 
			id_program_idx = df.columns.get_loc("ID_PROGRAM")
			nazwa_idx = df.columns.get_loc("NAZWA")

			# insert row values (created = True) or do nothing if already exists (created=False)
			_, created = Program.objects.get_or_create(
				id_program=row_values_list[id_program_idx],
				nazwa=row_values_list[nazwa_idx]
				)


	def insert_into_os_table(self, csv_file = '2_os.csv'):
				# read csv file
		df =  pd.read_csv(os.path.join(csv_files_directory, csv_file), sep=';')

		# iterate through dataframe and add rows to database
		for index, row in df.iterrows():
			# get a list of values stored in a row
			row_values_list = [df[label].values[index] for label in df.columns.to_list()]

			# get incides of df columns needed 
			id_program_idx = df.columns.get_loc("ID_PROGRAM")
			id_os_idx = df.columns.get_loc("ID_OS")
			nazwa_idx = df.columns.get_loc("NAZWA")

			# create Os instance providing existing objects as Foreign Keys
			os_obj = Os.objects.create(id_program=Program.objects.get(id_program=row_values_list[id_program_idx]),
										id_os = row_values_list[id_os_idx],
			 							nazwa=row_values_list[nazwa_idx])
			# save to db
			os_obj.save()

			return 0

	def insert_into_dzialanie_table(self, csv_file = '3_dzialanie.csv'):
				# read csv file
		df =  pd.read_csv(os.path.join(csv_files_directory, csv_file), sep=';')

		# iterate through dataframe and add rows to database
		for index, row in df.iterrows():
			# get a list of values stored in a row
			row_values_list = [df[label].values[index] for label in df.columns.to_list()]

			# get incides of df columns needed 
			id_program_idx = df.columns.get_loc("ID_PROGRAM")
			id_os_idx = df.columns.get_loc("ID_OS")
			id_dzialanie_idx = df.columns.get_loc("ID_DZIALANIE")
			nazwa_idx = df.columns.get_loc("NAZWA")

			# create Dzialanie instance providing existing objects as Foreign Keys
			os_dzialanie = Dzialanie.objects.create(id_program=Program.objects.get(id_program=row_values_list[id_program_idx]),
													id_os=Os.objects.get(id_os=row_values_list[id_os_idx]),
													id_dzialanie = row_values_list[id_dzialanie_idx],
			 										nazwa=row_values_list[nazwa_idx])
			# save to db
			os_dzialanie.save()

			return 0