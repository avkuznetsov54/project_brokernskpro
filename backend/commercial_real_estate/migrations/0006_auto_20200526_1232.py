# Generated by Django 3.0.6 on 2020-05-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial_real_estate', '0005_auto_20200525_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Способ покупки',
                'verbose_name_plural': 'Способы покупки',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='commercialestate',
            name='purchase_method',
            field=models.ManyToManyField(blank=True, default=None, related_name='comestate_purchasemethod', to='commercial_real_estate.PurchaseMethod', verbose_name='Способы покупки'),
        ),
    ]