# Filtry_Dzialan

Application created to **add** and **update** action filters structures (base FTD table and its FTD_Elementy elements; folder data/sql_files; 
files FTD.sql i FTD_Elementy.sql)

## INFO
As for ORM and REST API framework - Django was used.
Dummy json data (for task 2 and task 3) is stored in .json files (it would be received by functions from webapplication frontend)

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


## Usage

1. Clone repo
2. Install requirements from a file
```bash
pip install requirements.txt
```
3. Run server locally 
```bash
python manage.py runserver
```
4. Access url 'localhost:8000/action_filters/programs' to list all rows from Program table (task 2)
5. Access url 'localhost:8000/action_filters/add_filter' to add action filters structure to db (task 3). <br /> Update .json file to mock different JSON request.
6. Access url 'localhost:8000/action_filters/update_filter' to update existing action filters structure (task 4). <br />Update .json file to mock different JSON request.
7. REST API //TODO<br />