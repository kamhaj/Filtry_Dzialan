'''
Check if invoking a certain URL will trigger given class/view function.
'''

from filtry_dzialan_app.views import *
from django.urls import reverse, resolve
from filtry_dzialan_app.models import Program
from filtry_dzialan_app.views import *


class TestGeneralURLs():

	def test_api_overview_url(self):
	    found = resolve(reverse('filtry_dzialan_app:api-overview')) #resolving URL paths to the corresponding view function
	    print(found)
	    assert found.func == api_overview


class TestProgramURLs():

	def test_program_details_url(self):
	    found = resolve(reverse('filtry_dzialan_app:program-details', kwargs={'pk': '1'}))
	    print(found)
	    assert found.func == get_program_details

	def test_programs_list_url(self):
	    found = resolve(reverse('filtry_dzialan_app:programs-list'))
	    print(found)
	    assert found.func.view_class == ProgramsView


class TestFtdURLs():

	def test_action_filter_url(self):
	    found = resolve(reverse('filtry_dzialan_app:action_filter'))
	    print(found)
	    assert found.func.view_class == FtdElementyView
