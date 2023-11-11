# models.py
from django.db import models

class DataPasien(models.Model):
    noRekamMedis = models.IntegerField(primary_key=True)
    namaPasien = models.CharField(max_length=250)
    alamat = models.CharField(max_length=250)
    jenisKelamin = models.CharField(max_length=200, null=True)
    tanggalLahir = models.DateField()
    dokter = models.CharField(max_length=250)
    departemen = models.CharField(max_length=250)
    diagnosa = models.TextField(max_length=250)
    tindakan = models.TextField(max_length=250)

    def __str__(self):
        return self.namaPasien
