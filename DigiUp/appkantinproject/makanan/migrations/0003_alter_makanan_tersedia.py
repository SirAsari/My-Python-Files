# Generated by Django 4.1.3 on 2023-11-12 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makanan', '0002_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makanan',
            name='tersedia',
            field=models.CharField(choices=[('1', 'Tersedia'), ('0', 'Tidak Tersedia')], max_length=10),
        ),
    ]
