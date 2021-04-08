'''
unit tests examples for testing models

Django Tests: 	https://docs.djangoproject.com/en/3.1/topics/testing/overview/
PyTest: 		https://dev.to/lucasmiguelmac/pytest-with-django-rest-framework-from-zero-to-hero-8c4

'''

from django.test import TestCase
from filtry_dzialan_app.models import Program
from .factories import ProgramFactory
from model_bakery import baker


class ProgramTestCase(TestCase):
    def setUp(self):
        # make (save to db) or prepare (do not save to db)
        self.programs_batch = ProgramFactory.build_batch(3, nazwa="Dummy")
        self.program = ProgramFactory.create()
        self.program_override = ProgramFactory.create(nazwa='Moja nadpisana nazwa')

    def test_program_creation_batch(self, nazwa="Dummy"):
        program_obj = Program.objects.filter(nazwa=nazwa)
        self.assertEqual(len(self.programs_batch), 3)

    def test_get_progam_by_id(self, pk=1):
        program_obj = Program.objects.get(id_program=pk)
        self.assertEqual(program_obj.nazwa, 'Moja Test Nazwa')

    def test_get_progam_by_id_name_override(self, pk=2):
        program_obj = Program.objects.get(id_program=pk)
        self.assertEqual(program_obj.nazwa, 'Moja nadpisana nazwa')