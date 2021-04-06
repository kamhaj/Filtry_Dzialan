'''
help functions 
'''
import os

def get_all_files_in_path_with_given_extension(extension, folder_path):
	# get all ".extension" files
	files = [f for f in os.listdir(folder_path) if (os.path.isfile(os.path.join(folder_path, f)) and f.endswith(extension))]
	return sorted(files)


# insert into FTD and FTD_ELEMENTY tables some examples
def create_ftd_structure_dummy_data():
    pass