from django.shortcuts import render, HttpResponse
from .models import Program, Os, Dzialanie, Ftd, FtdElementy
from django.db import IntegrityError
import json
import os


## get all programs from PROGRAM table
def get_all_programs(request):
	programs = Program().get_all_programs()
	return render(request, 'programs.html', context={'programs': programs})



