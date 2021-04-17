'''
per app file to store factories
'''

from django.contrib.auth.models import User
from filtry_dzialan_app.models import Program
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'Kamil_{n}')
    email = factory.Sequence(lambda n: f'dummy_{n}@mycompany.com')
    password = factory.PostGenerationMethodCall(
        'set_password', 'kamilpassword123'
    )


class ProgramFactory(factory.django.DjangoModelFactory):
   
    class Meta:
        model = Program

    nazwa = 'Test Program'
