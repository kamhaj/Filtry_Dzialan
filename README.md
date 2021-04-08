# Filtry_Dzialan

Application created to **add** and **update** action filters structures (base FTD table and its FTD_Elementy elements; folder data/sql_files; 
files FTD.sql i FTD_Elementy.sql)

## INFO
As for ORM and REST API framework - Django was used. <br />
Dummy json data (for task 2 and task 3) is stored in .json files (it would be received by functions from webapplication frontend) <br />
As for testing framework PyTest was used  <br />
main.py file used for running db creation (company_database.sqlite3 file, task 1) <br />


## This task was accomplished in 6 steps:
- [x] task 1: <br />
writing a script to create a database based on provided .sql  (FTD structure) and .csv files (tables Program, Os, Dzialanie)  - db from this step is  company_db.sqlite3. It was created using task_1/db_creation_actions_filters_1.py script to automate (to some extent) creating tables from .csv files and later for django's inspectdb tool (to crete database models used in db.sqlite3 file - a database used futher from this point)
- [x] task 2: <br />
    creating a function that gets all rows from Program table in JSON format 
- [x] task 3: <br />
    creating a function that gets all rows from Program table in JSON format
- [x] task 4: <br />
    creating a function that gets all rows from Program table in JSON format
- [x] task 5: <br />
    writing tests to cover basic behaviours of functions from previous steps
- [x] task 6: <br /> 
    creating REST API for functions from previous steps (GET, POST, PUT)


## Where to look for task solutions:
1. Task 1: ./task_1/process.csv.files.py (CREATE TABLE statements from .csv files) <br />
and db_creation_actions_filters_1.py (creates company_database.sqlite3 file that is later use for Django 'inspectdb' tool to create db.sqlite3 - base project database)
2. Task 2: ./filtry_dzialan_app/views.py
3. Task 3: ./filtry_dzialan_app/views.py
4. Task 4: ./filtry_dzialan_app/views.py
5. Task 5: ./tests/test_filtry_dzalan_app
6. Task 6: ./filtry_dzialan_app/views.py (only task 2 for the moment)


## Usage

1. Clone repo
2. Activate virtual environment
3. Install requirements from a file
```bash
pip install requirements.txt
```
4. Run server locally (from where manage.py file is)
```bash
python manage.py runserver
```
5. In a browswer access "http://localhost:8000/action_filters/" to see proper URLs to all app functionalities.
6. Access url 'localhost:8000/action_filters/programs-list/' to list all rows from Program table
(task 2)
7. Access url 'localhost:8000/action_filters/add_action_filter/' to add action filters structure to db (task 3). <br /> Update .json file to mock different JSON request.
8. Access url 'localhost:8000/action_filters/update_action_filter/' to update existing action filters structure (task 4). <br />Update .json file to mock different JSON request.
9. REST API - only for (task 2) for the moment <br />


## TODO - IN PROGRESS
1. REST API add function (task 3)<br/> 
For now, add filter link works only with JSON file dummy data (dummy_add_action_filters_structure.json). We can create different action filter structure by modyfing it. 

2. REST API update function (task 4) <br/> 
For now, update filter link works only with JSON file dummy data (dummy_update_existing_action_filters_structure.json). We can update exiting action filter structure by modyfing it. Models are registered in Django Admin Panel (localhost:8000/admin) and it is an easy way to look for current
database state <br/> 

3. Create unit tests