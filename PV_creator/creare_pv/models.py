from django.db import models

class location(models.Model):
    id = models.IntegerField(
        primary_key=True,
        null=False,
        auto_created=True,
    )
    location_name = models.CharField(
        max_length=50,
        null=False
    )

class object_type(models.Model):
    id = models.IntegerField(
        primary_key=True,
        null=False,
        auto_created=True,
    )
    object_type = models.CharField(
        max_length=50,
        null= False
    )

class departament(models.Model):
    id = models.IntegerField(
        primary_key=True,
        null=False,
        auto_created=True,
    )
    departament_name = models.CharField(
        unique=True,
        max_length=50,
        null=False
    )
    id_locatie = models.ForeignKey(location, on_delete=models.PROTECT)

class department_object(models.Model):
    id = models.IntegerField(
        primary_key=True,
        null=False,
        auto_created=True
    )
    id_departament = models.ForeignKey(departament, on_delete=models.PROTECT)
    id_object_type = models.ForeignKey(object_type, on_delete=models.PROTECT)

class inv_number_management_by_departmant_and_location(models.Model):
    id = models.IntegerField(
        auto_created=True,
        null=False,
        primary_key=True
    )
    number_start = models.BigIntegerField(
        null=False,
        unique=True
    )
    number_stop = models.BigIntegerField(
        null=False,
        unique=True
    )
    id_departament = models.ForeignKey(departament, on_delete=models.PROTECT)
    id_locatie = models.ForeignKey(location, on_delete=models.PROTECT)

class person(models.Model):
    id = models.IntegerField(
        auto_created=True,
        null=False,
        primary_key=True
    )
    name = models.CharField(
        null=False,
        max_length=50
    )
    id_departament = models.ForeignKey(departament, on_delete=models.PROTECT)
    can_create_pv = models.BooleanField(
        default=False
    )

class db_inventar(models.Model):
    id = models.BigIntegerField(
        primary_key=True,
        null=False,
        auto_created=True
    )
    inv_number = models.PositiveBigIntegerField(
        unique=True,
        null=False,
    )
    id_departamant_object = models.ForeignKey(department_object, on_delete=models.PROTECT)
    object_description = models.CharField(
        max_length=100,
        null=False,
    )
    serial_number = models.CharField(
        max_length=75,
        null=False
    )
    id_persons = models.ForeignKey(person, on_delete=models.PROTECT)
    id_departament = models.ForeignKey(departament, on_delete=models.PROTECT)
    id_locatie = models.ForeignKey(location, on_delete=models.PROTECT)
    observations = models.CharField(
        max_length=256,
        null=True
    ) 

class creat_pv(models.Model):
    id = models.IntegerField(
        auto_created=True,
        null=False,
        primary_key=True
    )
    pv_type = models.CharField(
        null=False,
        max_length=10
    )
    recipient = models.ForeignKey(person, on_delete=models.PROTECT, related_name='pv_recipient')
    reqester = models.ForeignKey(person, on_delete=models.PROTECT, related_name='pv_reqester')
    nr_ticket = models.CharField(
        null=False,
        max_length=10
    )
    inv_number = models.ForeignKey(db_inventar, on_delete=models.PROTECT)