from django.core.exceptions import ValidationError
from django.db import models

import datetime


def generate_url_for_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/geo/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                now.hour, now.minute, now.second, now.microsecond, filename)
    return url


class Region(models.Model):
    """Модель Область"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')

    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Изображение")
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")

    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'
        ordering = ['name']


class City(models.Model):
    """Модель Город / Населенный пункт"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               verbose_name='Область',
                               related_name='city_region',
                               default=None,
                               null=True,
                               blank=False)

    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Изображение")
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город / Населенный пункт'
        verbose_name_plural = 'Города / Населенные пункты'
        ordering = ['id']


class District(models.Model):
    """Модель Района"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Район')
    subname = models.CharField(max_length=10, unique=True, verbose_name='Сокращённое название')
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             verbose_name='Город',
                             related_name='district_city',
                             default=None,
                             null=True,
                             blank=False)

    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Изображение")
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        ordering = ['name']


class Street(models.Model):
    """Модель Улица"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Улица')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        ordering = ['name']


class NumHouse(models.Model):
    """Модель Номер дома"""
    name = models.CharField(max_length=20, unique=True, verbose_name='Номер дома / корпуса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Номер дома'
        verbose_name_plural = 'Номера домов'
        ordering = ['name']


class Address(models.Model):
    """Модель Адрес (Улица и Номер дома)"""
    name = models.CharField(max_length=255, unique=True, blank=True, verbose_name='Адрес')
    street = models.ForeignKey(Street,
                               on_delete=models.SET_NULL,
                               verbose_name='Улица',
                               related_name='address_street',
                               null=True,
                               blank=False)
    numhouse = models.ForeignKey(NumHouse,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Номер дома / корпуса',
                                 related_name='address_numhouse',
                                 null=True,
                                 blank=False)

    def __str__(self):
        return self.name

    # Сохранияем "name" со значением "street" + "numhouse"
    # https://overcoder.net/q/1011394/django-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D1%83%D0%BD%D0%B8%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D1%8F%D0%B5%D0%BC%D0%BE%D0%B3%D0%BE-%D0%BF%D0%BE%D0%BB%D1%8F-%D0%B2-model-%D0%B0-%D1%82%D0%B0%D0%BA%D0%B6%D0%B5-%D0%B2-modelform
    def save(self, *args, **kwargs):
        if self.street is not None:
            self.name = '{} {}'.format(
                self.street.name,
                self.numhouse.name)
        else:
            self.name = str(self.street.name)
        super().save(*args, **kwargs)

    # Проверяем на уникальность поля name и выводим сообщение если есть дубль
    def clean(self):
        qs = self._meta.model.objects.exclude(pk=self.pk)
        qs = qs.filter(
            street=self.street,
            numhouse=self.numhouse)
        if qs.exists():
            raise ValidationError('Такой адрес уже существует.')

    class Meta:
        verbose_name = 'Адрес (Улица и Номер дома)'
        verbose_name_plural = 'Адреса (Улицы и Номера домов)'
        ordering = ['name']

