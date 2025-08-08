from django.db import models

class Locations(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class ObjectTypes(models.Model):
    name = models.CharField(
        max_length=20,
    )

class Departaments(models.Model):
    name = models.CharField(
        max_length=50,
    )
    location = models.ForeignKey(Locations, on_delete=models.SET_DEFAULT, related_name='department', default=None)

class DepartmentObjects(models.Model):
    departament = models.ForeignKey(Departaments, on_delete=models.SET_DEFAULT, related_name='object', default=None)
    objectType = models.ForeignKey(ObjectTypes, on_delete=models.SET_DEFAULT, related_name='object', default=None)

class InventoryClasses(models.Model):
    name = models.CharField(
        max_length=50,
    )
    limitMin = models.IntegerField(
        unique=True,
    )
    limitMax = models.IntegerField(
        unique=True,
    )
    departament = models.ForeignKey(Departaments, on_delete=models.SET_DEFAULT, related_name='inventoryClass', default=None)

class Persons(models.Model):
    name = models.CharField(
        max_length=50,
    )
    departament = models.ForeignKey(Departaments, on_delete=models.SET_DEFAULT, related_name='person', default=None)

class Assets(models.Model):
    invNumber = models.PositiveBigIntegerField(
        unique=True,
    )
    inventoryClass =  models.ForeignKey(InventoryClasses, on_delete=models.SET_DEFAULT, related_name='asset', default=None)
    objectType = models.ForeignKey(ObjectTypes, on_delete=models.SET_DEFAULT, related_name='asset', default=None)
    departament = models.ForeignKey(Departaments, on_delete=models.SET_DEFAULT, related_name='asset', default=None)
    description = models.CharField(
        max_length=100,
        null=False,
    )
    serialNumber = models.CharField(
        max_length=200,
    )
    imei = models.CharField(
        max_length=18,
    )
    person = models.ForeignKey(Persons, on_delete=models.SET_DEFAULT, related_name='asset', default=None)
    observations = models.CharField(
        max_length=256,
        null=True,
        blank=True
    ) 

    # TODO: Constrante pentru numerele de inventar
    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             check=models.Q(invNumber__gte=InventoryClasses.limitMin) & models.Q(invNumber__lte=InventoryClasses.limitMax) & models.Q(departament__exact=InventoryClasses.departament),
    #             name="invNumberValidaton"
    #         )
    #     ]

class PV(models.Model):
    pvType = models.CharField(
        max_length=10,
    )
    recipient = models.ForeignKey(Persons, on_delete=models.SET_DEFAULT, related_name='recipient', default=None)
    reqester = models.ForeignKey(Persons, on_delete=models.SET_DEFAULT, related_name='requester', default=None)
    nrTicket = models.CharField(
        max_length=10,
    )
    invNumber = models.ForeignKey(Assets, on_delete=models.SET_DEFAULT, related_name='pv', default=None)
