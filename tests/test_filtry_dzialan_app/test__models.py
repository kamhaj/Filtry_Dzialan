'''
unit tests examples for testing models

testing models is basically checking if we can work with the model (CRUD operations)

if some default methods (e.g. save()) were overridden, then they should be tested too
'''

from django.test import TestCase
from filtry_dzialan_app.models import Program, Os, Dzialanie
from .factories import ProgramFactory
from model_bakery import baker
import pytest


@pytest.mark.django_db
class TestProgramModel():   

    def test_create_new_program(self):
        program = ProgramFactory()
        # Check all field and validators
        program.clean_fields()  #  EXCLUDE: FK, O2O, M2M Fields
        
        # Check we can find it
        programs = Program.objects.all()
        assert len(programs) == 1

        first_program = programs[0]
        assert first_program == program


    @pytest.mark.django_db
    def test_check_attribute_in_program(self):
        # Check attributes
        program = ProgramFactory()
        assert program.nazwa == 'Test Program'


    @pytest.mark.django_db
    def test_check_str_representation_of_program(self):
        # Check string representation
        program = ProgramFactory(nazwa="Moj Test Program")
        assert program.__str__() == f'Program numer 1: Moj Test Program'