from django.db import models

class Toko(models.Model):
    nama = models.CharField(max_length=255)
    telpon = models.CharField(max_length=15)
    alamat = models.TextField()

class Barang(models.Model):
    nama = models.CharField(max_length=255)
    keterangan = models.TextField()
    harga = models.IntegerField()
    gambar = models.ImageField(upload_to='barang/images/')
    stok = models.IntegerField()
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
