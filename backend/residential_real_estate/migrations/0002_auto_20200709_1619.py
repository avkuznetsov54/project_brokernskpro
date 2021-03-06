# Generated by Django 3.0.6 on 2020-07-09 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo_location', '0003_auto_20200606_1303'),
        ('residential_real_estate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residentialcomplex',
            name='address',
        ),
        migrations.AddField(
            model_name='residentialcomplex',
            name='num_house',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_numhouse', to='geo_location.NumHouse', verbose_name='Номер дома/строения/корпус'),
        ),
        migrations.AddField(
            model_name='residentialcomplex',
            name='street',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rescomplex_street', to='geo_location.Street', verbose_name='Улица'),
        ),
    ]
