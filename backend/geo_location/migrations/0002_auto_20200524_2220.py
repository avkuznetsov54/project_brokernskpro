# Generated by Django 3.0.6 on 2020-05-24 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_location', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Город / Населенный пункт', 'verbose_name_plural': 'Города / Населенные пункты'},
        ),
    ]
