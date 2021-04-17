'''
serialize data to JSON
'''

from rest_framework import serializers
from .models import Program, Os, Dzialanie, Ftd, FtdElementy
from django.shortcuts import HttpResponse

class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        # model to be serialized
        model = Program 					
        # fields to be displayed
        fields = (
            'id_program', 
            'nazwa') 	



class OsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Os
        fields = (
            'id_program', 
            'id_os', 
            'nazwa')


class DzialanieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dzialanie
        fields = (
            'id_program', 
            'id_os', 
            'id_dzialanie', 
            'nazwa')



class FtdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ftd
        fields = (
            'id_ftd', 
            'nazwa', 
            'opis')


class FtdElementySerializer(serializers.ModelSerializer):
    id_ftd = FtdSerializer()

    class Meta:
        model = FtdElementy
        fields = ('id_ftd_element', 'id_ftd') #('id_ftd_element', 'id_ftd', 'id_dzialanie')


    def create(self, validated_data):
        ftd_instance = Ftd.objects.create(**validated_data.pop('id_ftd'))       # nazwa + opis
        ftd_instance.save()

        # get dzialanie in loop (no need to change them, just assigning them) and create row in FtdElementy table
        id_dzialanie_list = validated_data.pop('id_dzialanie_list')
        for id_dzialanie in id_dzialanie_list:
            try:
                dzialanie_instance = Dzialanie.objects.get(pk=id_dzialanie)
            except Dzialanie.DoesNotExist:
                    return HttpResponse(status=status.HTTP_404_NOT_FOUND)
            ftd_elementy_instance = FtdElementy.objects.create(id_ftd=ftd_instance, 
                                        id_dzialanie=dzialanie_instance) #, **modela_data)
            ftd_elementy_instance.save()

        return 0

    def update(self, validated_data):
        ftd_data = validated_data.pop('id_ftd')
        ftd_instance = Ftd.objects.get(pk=ftd_data['id_ftd'])       # nazwa + opis
        
        # update ftd info, leave old cretion date
        ftd_instance.nazwa = ftd_data['nazwa']
        ftd_instance.opis = ftd_data['opis']
        ftd_instance.save()

        # get existing ftd_elementy rows for given ftd object and delete them
        FtdElementy.objects.filter(id_ftd=ftd_instance.id_ftd).delete()

        # get dzialanie in loop (no need to change them, just assigning them) and create row in FtdElementy table
        id_dzialanie_list = validated_data.pop('id_dzialanie_list')
        for id_dzialanie in id_dzialanie_list:
            try:
                dzialanie_instance = Dzialanie.objects.get(pk=id_dzialanie)
            except Dzialanie.DoesNotExist:
                    return HttpResponse(status=status.HTTP_404_NOT_FOUND)
            ftd_elementy_instance = FtdElementy.objects.create(id_ftd=ftd_instance, 
                                        id_dzialanie=dzialanie_instance) #, **modela_data)
            ftd_elementy_instance.save()

        return 0