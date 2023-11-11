# Generated by Django 4.1.3 on 2023-11-11 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=250)),
                ('isbn', models.CharField(max_length=13)),
                ('pengarang', models.CharField(max_length=250)),
                ('sinopsis', models.TextField(blank=True, null=True)),
                ('tanggal_rilis', models.DateField()),
                ('jumlah_halaman', models.IntegerField()),
                ('gambar', models.ImageField(upload_to='movie/images/')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.publisher')),
            ],
        ),
    ]
