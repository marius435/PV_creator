from django.db import models

class Locations(models.Model):
    name = models.CharField(
        max_length=50,
    )

class ObjectTypes(models.Model):
    name = models.CharField(
        max_length=50,
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
    )# TODO: Create constrain based on InventoryClasses 
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
    def __str__(self):
        a= str(self.inv_number)
        return a
    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             check=models.Q(invNumver__gte=InventoryClasses.limitMin) & models.Q(invNumber__lte=InventoryClasses.limitMax) & models.Q(departmant__exact=InventoryClasses.departament)
    #         ),
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
