'''
unit tests examples for testing functions from files 1_, 2_ and 34_

created using pytest

run using 
'''
import pytest


def test__example():
	assert 1 == 1


## do we need fixture here?
@pytest.mark.task_1
class Test__DatabaseCreation:

	## test db connection
	def test__db_connection(self):
		pass

	## test if user is superuser
	def test__my_user(self):
    	#me = User.objects.get(username='me')
        #assert me.is_superuser
		pass