# Generated by Django 4.1.3 on 2023-11-11 03:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('telpon', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='min 8 digit', regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='gambar',
            field=models.ImageField(upload_to='movie/images/'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.publisher'),
            preserve_default=False,
        ),
    ]
