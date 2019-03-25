from django.db import models

from django.db import models

CAT = (
    ('AMP', 'Amplifier'), ('CON', 'Controller'), ('SPK', 'Speaker'), ('CAT6TX', 'CAT6 Tx'),
    ('CAT6RX', 'CAT6 Rx'), ('LC', 'Lecture Capture'), ('TP', 'Touch Panel'), ('LCDMON', 'LCD Monitor'),
)


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=50)

    def __str__(self):
        return self.manufacturer


class EquipmentModel(models.Model):
    model_number = models.CharField(max_length=50)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    def __str__(self):
        return self.model_number


class Device(models.Model):

    ins_ref = models.CharField(max_length=6, primary_key=True)

    category = models.CharField(max_length=50, choices=CAT, blank=False)

    fbs_ref = models.IntegerField()
    model = models.ForeignKey('EquipmentModel', on_delete=models.CASCADE, null=True, blank=True)
    serial_number = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=20)
    ip = models.GenericIPAddressField(protocol='IPv4', unpack_ipv4=False, null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
    comments = models.TextField(blank=True)

    def __int__(self):
        return self.ins_ref


class Location(models.Model):
    location = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.location
