from django.shortcuts import render
from .models import Program, Os, Dzialanie, Ftd, FtdElementy
import json
from django.db import IntegrityError



## get all programs from PROGRAM table
def get_all_programs(request):
	programs = Program().get_all_programs()
	return render(request, 'programs.html', context={'programs': programs})



## add row to a database in FTD table (task 3)
def add_action_filter_with_structure(request):
	dummy_filter_structure_json = {
		"nazwa": "test nazwa filtra",
		"opis": "test opis filtra",
		"dzialania": [
			{"id": 4702},
           	{"id": 4709},
           	{"id": 4725},
            {"id": 5530}
    	]
	}

	# TODO: make both saves as transaction, rollback if any problem occurs

	ftd = Ftd.objects.create(nazwa=dummy_filter_structure_json['nazwa'],
							opis=dummy_filter_structure_json['opis'])

	# save to db
	ftd.save()


	# iterate through dzialania ids from  JSON response
	for json_dzialanie in dummy_filter_structure_json["dzialania"]:
		id_dzialanie = json_dzialanie.get('id')

		ftd_elementy_obj = FtdElementy.objects.create(id_ftd=Ftd.objects.get(id_ftd=ftd.pk),
											id_dzialanie = Dzialanie.objects.get(id_dzialanie=id_dzialanie))
		# save to db
		ftd_elementy_obj.save()

	return render(request, 'add_filter.html', context={'dummy_filter_structure_json': dummy_filter_structure_json})


## update row to a database in FTD table (task 4)
def update_action_filter_with_structure(request):
	dummy_filter_structure_json = {
		"id_ftd": 11,
		"nazwa": "update nazwy filtra poprzez funkcje",
		"opis": "update opisu filtra poprzez funkcje",
		"dzialania_do_odznaczenia": [
			{"id": 4702},
           	{"id": 4725},
    	],
    	"dzialania_do_zaznaczenia": [
			{"id":6594},
           	{"id": 6590},
           	{"id": 5064}
    	]
	}

	# check if specified action filter exists (it should, since we are modyfing it)
	try:
		Ftd.objects.filter(id_ftd=dummy_filter_structure_json['id_ftd']).update(nazwa=dummy_filter_structure_json['nazwa'], opis=dummy_filter_structure_json['opis'])
	except IntegrityError as e: 	# if any constraint was violated
		print('Specified filter does not exist. Exception: {}'.format(e.message))
		raise Exception(e)


	# filter ftd_elementy rows with specified id_ftd
	ftd_elementy_rows = FtdElementy.objects.filter(id_ftd=dummy_filter_structure_json["id_ftd"])

	''' delete filter structures '''
	# iterate through dzialania ids from  JSON response
	for json_dzialanie in dummy_filter_structure_json["dzialania_do_odznaczenia"]:
		id_dzialanie = json_dzialanie.get('id')

		# filter ftd_elementy rows with specified id_ftd and from this subset get ftd_element with given id
		ftd_elementy_rows = FtdElementy.objects.filter(id_ftd=dummy_filter_structure_json["id_ftd"])
		ftd_element = ftd_elementy_rows.get(id_dzialanie=id_dzialanie)

		# delete from db
		ftd_element.delete()
	

	''' update filter structures '''
	# iterate through dzialania ids from  JSON response
	for json_dzialanie in dummy_filter_structure_json["dzialania_do_zaznaczenia"]:
		id_dzialanie = json_dzialanie.get('id')

		# create object
		ftd_element = FtdElementy.objects.create(id_ftd=Ftd.objects.get(id_ftd=dummy_filter_structure_json['id_ftd']),
											id_dzialanie = Dzialanie.objects.get(id_dzialanie=id_dzialanie))


		# save to db
		ftd_element.save()
	


	# check if FTD has any FTD_ELEMENTY rows left. If not - delete bases FTD.
	ftd_elements_queryset = FtdElementy.objects.filter(id_ftd=dummy_filter_structure_json['id_ftd'])
	if not ftd_elements_queryset:
		Ftd.objects.get(id_ftd=dummy_filter_structure_json['id_ftd']).delete()

	return render(request, 'update_filter.html', context={'dummy_filter_structure_json': dummy_filter_structure_json})



	'''

	    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)


    '''