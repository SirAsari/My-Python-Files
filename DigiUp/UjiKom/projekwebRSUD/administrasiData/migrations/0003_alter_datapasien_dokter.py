# Generated by Django 4.1.3 on 2023-11-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasiData', '0002_alter_book_dokter_alter_book_norekammedis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapasien',
            name='dokter',
            field=models.CharField(max_length=250),
        ),
    ]