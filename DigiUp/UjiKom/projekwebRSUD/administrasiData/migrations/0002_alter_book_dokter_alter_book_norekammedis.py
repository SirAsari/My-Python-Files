# Generated by Django 4.1.3 on 2023-11-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasiData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapasien',  
            name='dokter',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='datapasien',  
            name='noRekamMedis',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
