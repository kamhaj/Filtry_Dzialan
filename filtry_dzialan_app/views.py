'''
Zadania widoku:

gromadzi dane do renderowania przy użyciu metod menedżera
inicjowanie formularzy
renderowanie szablonów
W widokach nie powinieneś:

sprawdzanie poprawności danych - za to jest odpowiedzialność formularz
zapisywać danych - to jest odpowiezialność formularza
budowanie złożonych zapytań - to jest odpowiedzialność menedżera

'''

from django.shortcuts import render, HttpResponse
from .models import Program, Os, Dzialanie, Ftd, FtdElementy
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view 	# function based views API
from rest_framework.response import Response
from .serializers import ProgramSerializer, FtdSerializer, FtdElementySerializer
from rest_framework import status
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET'])
def api_overview(request):
	api_urls = {
		'Get program details': '/program-details/<str:pk>/',
		'Get programs list': '/programs-list/',
		'Create/Update action filter structure': '/action_filter/'
	}

	# return API response
	return Response(api_urls)


## seperate GET method for obtaining single Program details
@api_view(['GET'])
def get_program_details(request, pk):
	# query db and serialize data
	try:
		program =  Program.objects.get(id_program=pk)
	except Program.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)
	serializer = ProgramSerializer(program)
	return Response(serializer.data)


class ProgramsView(APIView):

    #permission_classes = (IsAuthenticated, )

    ## get all objects from db
    def get(self, request, *args, **kwargs):
    	# get queryset 
        qs = Program.objects.all()
        # set up serializer (no need to validate data, it's coming straight from the database)
        serializer = ProgramSerializer(qs, many=True)
        return Response(serializer.data)

    ## create one object
    def post(self, request, *args, **kwargs):
    	# serialize user input
        serializer = ProgramSerializer(data=request.data)
        # validate user  input, save to db if ok, return errors if not
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # def delete(self, request, *args, **kwargs)...
    # def put(self, request, *args, **kwargs)...


class FtdElementyView(APIView):

    ## get all objects from db
    def get(self, request, *args, **kwargs):
        # get queryset 
        qs = FtdElementy.objects.all()
        # set up serializer (no need to validate data, it's coming straight from the database)
        serializer = FtdElementySerializer(qs, many=True)
        return Response(serializer.data)


    ## create one object
    ''' JSON example
	{        
		"id_ftd": {
            "nazwa": "stworz moj nowy filtr dzialan",
            "opis": "moj nowy filtr dzialan"
        },
        "id_dzialanie_list": [4709,6669, 6670, 6671]
	}
    '''
    def post(self, request, *args, **kwargs):
    	# serialize user input
        serializer = FtdElementySerializer(data=request.data)
        # validate user  input, save to db if ok, return errors if not
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    ## update one object
    ''' JSON example - bylo 4709 i 6669
	{        
		"id_ftd": {
			"id_ftd": 22,
            "nazwa": "filtr dzialan update rest api",
            "opis": "rest api test"
        },
        "id_dzialanie_list": [6669, 6670]
	}
	- delete any existing and assign id_dzialanie from given list  
	- update id_ftd info
    '''
    def put(self, request, format=None):
    	# serialize user input
        serializer = FtdElementySerializer(data=request.data)
        # validate user  input, save to db if ok, return errors if not
        if serializer.is_valid():
            serializer.update(request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
