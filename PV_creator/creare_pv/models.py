from django.db import models

# Create your models here.
class Pv_type_operation(models.TextChoices):
    primire = 'PRIMIRE', 'primire'
    predare = 'PREDARE', 'predare'

class Addressing(models.TextChoices):
    dl = 'Dl', 'Dl'
    dna = 'Dna', 'Dna'

class Ticket(models.Model):
    pv_type = models.CharField(
        max_length=10,
        choices=Pv_type_operation.choices,
        default=Pv_type_operation.primire,
        help_text='Selectati daca este un proces verbal de primire sau de predare.'
    )

    pers1_addressing = models.CharField(
        max_length=5,
        choices=Addressing.choices,
        default=Addressing.dl
    )

    pers1_name = models.CharField(
        max_length=50,
        null=False
    )

    pers2_addressing = models.CharField(
        max_length=5,
        choices=Addressing.choices,
        default=Addressing.dl
    )

    pers2_name = models.CharField(
        max_length=50,
        null=False
    )

    inventar_number = models.PositiveBigIntegerField(
        verbose_name='Inventar'
    )

    object_description = models.CharField(
        max_length=256,
        null=False
    )

    serian_number = models.CharField(
        max_length=25
    )

    imei = models.CharField(
        max_length = 25
    )

    def __str__(self):
        return str(self.inventar_number)