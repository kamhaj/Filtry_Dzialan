from django.shortcuts import render, HttpResponse
from .models import Program, Os, Dzialanie, Ftd, FtdElementy
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view 	# function based views API
from rest_framework.response import Response
from .serializers import ProgramSerializer, FtdSerializer, FtdElementySerializer
from rest_framework import status
import json
#import os


@api_view(['GET'])
def api_overview(request):
	api_urls = {
		'Get program details': '/program-details/<str:pk>/',
		'Get programs list': '/programs-list/',
		'Create action filter structure': '/add_action_filter/',
		'Update action filter structure': '/update_action_filter/<str:pk>/',
		'Get action filter JSON example': '/get_ftd/<str:pk>/'
	}

	# return API response
	return Response(api_urls)


## get all programs from PROGRAM table
@api_view(['GET'])
def get_all_programs(request):
	# query db and serialize data
	programs =  Program.objects.all()
	serializer = ProgramSerializer(programs, many=True)	# many True for more than 1 item

	# return API response
	return Response(serializer.data)


## get one programs from PROGRAM table
@api_view(['GET'])
def get_program_details(request, pk):
	# query db and serialize data
	programs =  Program.objects.get(id_program=pk)
	serializer = ProgramSerializer(programs, many=False)	# many False for 1 item

	# return API response
	return Response(serializer.data)


## add row to a database in FTD table (task 3) using API
@api_view(['POST'])
def add_action_filter_with_structure_api(request, json_filepath='dummy_add_action_filters_structure.json'):
	# get serializer
	serializer = FtdElementySerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# TODO: make all saves as transaction, rollback if any error occurs


## add row to a database in FTD table (task 3)
def add_action_filter_with_structure(request, json_filepath='dummy_add_action_filters_structure.json'):
	# open dummy file
	with open(json_filepath) as json_file:
		json_request = json.load(json_file)

	# TODO: make all saves as transaction, rollback if any error occurs

	# create a new ftd object and save it to db
	try:
		ftd = Ftd.objects.create(nazwa=json_request['nazwa'],
								opis=json_request['opis'])
	except Ftd.DoesNotExist:
		return HttpResponse(status=404)
	
	ftd.save()

	# iterate through dzialania ids from  JSON request, save each one to db
	for json_dzialanie in json_request["dzialania"]:
		id_dzialanie = json_dzialanie.get('id')
		ftd_elementy_obj = FtdElementy.objects.create(id_ftd=Ftd.objects.get(id_ftd=ftd.pk),
											id_dzialanie = Dzialanie.objects.get(id_dzialanie=id_dzialanie))
		ftd_elementy_obj.save()

	return render(request, 'add_filter.html', context={'json_request': json_request})


## update row to a database in FTD table (task 4)
def update_action_filter_with_structure(request, json_filepath='dummy_update_existing_action_filters_structure.json'):
	# open dummy file
	with open(json_filepath) as json_file:
		json_request = json.load(json_file)

	# TODO: make all saves as transaction, rollback if any error occurs

	# check if specified action filter exists (it should, since we are modyfing it)
	try:
		Ftd.objects.filter(id_ftd=json_request['id_ftd']).update(nazwa=json_request['nazwa'], opis=json_request['opis'])
	except IntegrityError as e: 	# if any constraint was violated
		print('Specified filter does not exist. Exception: {}'.format(e.message))
		raise Exception(e)
	except Ftd.DoesNotExist:
		return HttpResponse(status=404)

	# filter ftd_elementy rows with specified id_ftd
	ftd_elementy_rows = FtdElementy.objects.filter(id_ftd=json_request["id_ftd"])

	''' delete filter structures from db'''
	# iterate through dzialania ids from  JSON response
	for json_dzialanie in json_request["dzialania_do_odznaczenia"]:
		id_dzialanie = json_dzialanie.get('id')

		# filter ftd_elementy rows with specified id_ftd and from this subset get ftd_element with given id
		ftd_elementy_rows = FtdElementy.objects.filter(id_ftd=json_request["id_ftd"])
		ftd_element = ftd_elementy_rows.get(id_dzialanie=id_dzialanie)
		ftd_element.delete()
	

	''' update filter structures in db '''
	# iterate through dzialania ids from  JSON response
	for json_dzialanie in json_request["dzialania_do_zaznaczenia"]:
		id_dzialanie = json_dzialanie.get('id')

		# create object and save to db
		ftd_element = FtdElementy.objects.create(id_ftd=Ftd.objects.get(id_ftd=json_request['id_ftd']),
											id_dzialanie = Dzialanie.objects.get(id_dzialanie=id_dzialanie))
		ftd_element.save()
	

	# check if FTD has any FTD_ELEMENTY rows left. If not - delete bases FTD.
	ftd_elements_queryset = FtdElementy.objects.filter(id_ftd=json_request['id_ftd'])
	if not ftd_elements_queryset:
		Ftd.objects.get(id_ftd=json_request['id_ftd']).delete()

	return render(request, 'update_filter.html', context={'json_request': json_request})
