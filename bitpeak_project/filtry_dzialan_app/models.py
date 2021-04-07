# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core import serializers
from django.utils.timezone import now


class Program(models.Model):
    id_program = models.AutoField(primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='NAZWA', max_length=100)  # Field name made lowercase.

    ## get all Program table entries in JSON format
    def get_all_programs(self):
        # get query set using ORM
        queryset = Program.objects.all()

        # get JSON serializer
        JSONSerializer = serializers.get_serializer("json")
        json_serializer = JSONSerializer()
        json_serializer.serialize(queryset)     #,  fields=('nazwa', ...) --> optional

        data = json_serializer.getvalue()
        return json_serializer.getvalue()

    ## get single Program table row using PK in JSON format
    def get_program_by_id(self, primary_key_id):
        ##TODO - JSON parse
        return Program.objects.get(id_program=primary_key_id)


    ## TODO - delete, update methods...

    def __str__(self):
        return f"Program numer {self.id_program}: {self.nazwa}"

    class Meta:
        # add any constraints here...
        managed = True      ## to allow Django to modify table
        db_table = 'PROGRAM'




class Os(models.Model):
    id_program = models.ForeignKey('Program',  on_delete=models.DO_NOTHING, db_column='ID_PROGRAM', related_name="id_os")  # Field name made lowercase.
    id_os = models.AutoField(primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='NAZWA', max_length=100)  # Field name made lowercase.


    def __str__(self):
        return f"Os numer {self.id_os}: {self.nazwa}"


    class Meta:
        # add any constraints here...
        managed = True      ## to allow Django to modify table
        db_table = 'OS'
              
        
        
class Dzialanie(models.Model):
    id_program = models.ForeignKey('Program', on_delete=models.DO_NOTHING, db_column='ID_PROGRAM', related_name="fk_program_dzialanie") 
    id_os = models.ForeignKey('Os', on_delete=models.DO_NOTHING, db_column='ID_OS', related_name="fk_os_dzialanie")  # Field name made lowercase.
    id_dzialanie = models.AutoField(primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='NAZWA', max_length=100)  # Field name made lowercase.


    def __str__(self):
        return f"Dzialanie numer {self.id_dzialanie}: {self.nazwa}"

    class Meta:
        # add any constraints here...
        managed = True      ## to allow Django to modify table
        db_table = 'DZIALANIE'         
        


class Ftd(models.Model):
    id_ftd = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(blank=True, null=True, max_length=300)      # it's now nullable
    data_utworzenia = models.DateField(default=now, editable=True)


    def __str__(self):
        return f"FTD numer {self.id_ftd}: {self.nazwa}"


    class Meta:
        # add any constraints here...
        managed = True      ## to allow Django to modify table
        db_table = 'FTD'



class FtdElementy(models.Model):
    id_ftd_element = models.AutoField(primary_key=True)
    id_ftd = models.ForeignKey('Ftd', models.DO_NOTHING, db_column='id_ftd')
    id_dzialanie = models.ForeignKey('Dzialanie', on_delete=models.DO_NOTHING, db_column='ID_DZIALANIE', related_name="fk_ftd_elementy_dzialanie")


    def __str__(self):
        return f"FTD Element numer {self.id_ftd_element} ({self.id_ftd})"

    class Meta:
        # add any constraints here...
        managed = True      ## to allow Django to modify table
        db_table = 'FTD_ELEMENTY'