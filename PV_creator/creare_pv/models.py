from django.db import models

class location(models.Model):
    location_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

class object_type(models.Model):
    object_type = models.CharField(
        max_length=50,
        null= False,
        blank=False
    )

class departament(models.Model):
    departament_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    id_locatie = models.ForeignKey(location, on_delete=models.PROTECT)

class department_object(models.Model):
    id_departament = models.ForeignKey(departament, on_delete=models.PROTECT)
    id_object_type = models.ForeignKey(object_type, on_delete=models.PROTECT)

class inv_number_management_by_departmant_and_location(models.Model):
    number_start = models.BigIntegerField(
        null=False,
        unique=True,
        blank=False
    )
    number_stop = models.BigIntegerField(
        null=False,
        unique=True,
        blank=False
    )
    id_departament = models.ForeignKey(departament, on_delete=models.PROTECT)
    id_locatie = models.ForeignKey(location, on_delete=models.PROTECT)

class person(models.Model):
    name = models.CharField(
        null=False,
        max_length=50,
        blank=False
    )
    id_departament = models.ForeignKey(departament, on_delete=models.PROTECT)
    can_create_pv = models.BooleanField(
        default=False
    )

class db_inventar(models.Model):
    inv_number = models.PositiveBigIntegerField(
        unique=True,
        null=False,
        blank=False
    )
    id_departamant_object = models.ForeignKey(department_object, on_delete=models.PROTECT)
    object_description = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    serial_number = models.CharField(
        max_length=75,
        null=False,
        blank=False
    )
    id_persons = models.ForeignKey(person, on_delete=models.PROTECT)
    id_departament = models.ForeignKey(departament, on_delete=models.PROTECT)
    id_locatie = models.ForeignKey(location, on_delete=models.PROTECT)
    observations = models.CharField(
        max_length=256,
        null=True,
        blank=False
    ) 
    def __str__(self):
        a= str(self.inv_number)
        return a

class creat_pv(models.Model):
    pv_type = models.CharField(
        null=False,
        max_length=10,
        blank=False
    )
    recipient = models.ForeignKey(person, on_delete=models.PROTECT, related_name='pv_recipient')
    reqester = models.ForeignKey(person, on_delete=models.PROTECT, related_name='pv_reqester')
    nr_ticket = models.CharField(
        null=False,
        max_length=10,
        blank=False
    )
    inv_number = models.ForeignKey(db_inventar, on_delete=models.PROTECT)
