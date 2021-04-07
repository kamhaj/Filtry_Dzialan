'''
serialize data to JSON
'''

from rest_framework import serializers
from .models import Program, Os, Dzialanie, Ftd, FtdElementy


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program 					# model to be serialized
        fields = ('id_program', 'nazwa') 	# fields to be displayed



class OsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Os
        fields = ('id_program', 'id_os', 'nazwa')


class DzialanieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dzialanie
        #fields = ('id_program', 'id_os', 'id_dzialanie', 'nazwa')
        fields = ('id_dzialanie',)



class FtdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ftd
        #fields = ('id_ftd', 'nazwa', 'opis')
        fields = ('id_ftd',)


class FtdElementySerializer(serializers.ModelSerializer):
    id_ftd = FtdSerializer()
    id_dzialanie = DzialanieSerializer()

    class Meta:
        model = FtdElementy
        fields = ('id_ftd_element', 'id_dzialanie', 'id_ftd') #('id_ftd_element', 'id_ftd', 'id_dzialanie')

    # override create method
    def create(self, validated_data):
        # add code to loop over 'id_ftd_element' IDs from JSON request...

        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        id_ftd = validated_data.pop('id_ftd').get('id_ftd')
        id_dzialanie = validated_data.pop('id_dzialanie').get('id_dzialanie')

        # get (or create if does not exist) instances
        ftd_instance, created = Ftd.objects.get_or_create(id_ftd=id_ftd)
        dzialanie_instance = Dzialanie.objects.get(id_dzialanie=id_dzialanie)

        # create ftd_element_instance and save to db
        ftd_element_instance = FtdElementy.objects.create(**validated_data, 
                                                            id_ftd=ftd_instance,
                                                            id_dzialanie=dzialanie_instance)
        ftd_element_instance.save()

        return ftd_element_instance


    # # override update method. Modify example code.
    # def update(self, instance, validated_data):
    #     albums_data = validated_data.pop('album_musician')
    #     albums = (instance.album_musician).all()
    #     albums = list(albums)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.instrument = validated_data.get('instrument', instance.instrument)
    #     instance.save()

    #     for album_data in albums_data:
    #             album = albums.pop(0)
    #             album.name = album_data.get('name', album.name)
    #             album.release_date = album_data.get('release_date', album.release_date)
    #             album.num_stars = album_data.get('num_stars', album.num_stars)
    #             album.save()
    #     return instance

