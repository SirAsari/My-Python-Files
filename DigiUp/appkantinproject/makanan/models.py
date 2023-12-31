from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Kantin(models.Model):
    nama = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Min 8 digit")
    telpon = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    def __str__(self) -> str:
        return self.nama
    
class Makanan(models.Model):
    nama = models.CharField(max_length=250)
    harga = models.IntegerField()
    gambar = models.ImageField(upload_to='movie/images/')
    stok = models.IntegerField()
    kantin = models.ForeignKey(Kantin, on_delete=models.CASCADE)
    TERSEDIA = (
        ('1', 'Tersedia'),
        ('0', 'Tidak Tersedia'),
    )
    tersedia = models.CharField(max_length=10, choices=TERSEDIA)
    def __str__(self) -> str:
        return self.nama

class CartItem(models.Model):
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)