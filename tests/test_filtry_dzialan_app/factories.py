'''
per app file to store factories
'''

import factory		# for making/preparing model instances
from filtry_dzialan_app.models import Program

class ProgramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Program

    nazwa = 'Moja Test Nazwa'