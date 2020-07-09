import os
from django.core.exceptions import ValidationError as DjangoValidationError

from django.db import models

import datetime

from slugify import slugify  # тут используется awesome-slugify
from PIL import Image  # для обработки изображения нам нужен pillow

from project import settings
from geo_location.models import Region, City, District, Address


# ф-ция генерит путь для загружаемого изображения
def generate_url_for_image(self, filename):
    # проверяет в какой model была фызвана ф-ция, и бирёт нужный атрибут для имени файла
    if hasattr(self, 'name'):
        name_file = self.name
    # elif hasattr(self, 'residential_complex'):
    #     name_file = self.residential_complex.name
    elif hasattr(self, 'alt_attr') and self.alt_attr != '':
        name_file = self.alt_attr
    else:
        name_file = 'residential_complex_image'

    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    filename = "%s.%s" % (slugify(name_file, to_lower=True), ext)
    now = datetime.datetime.now()
    url = 'images/realestate/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                       now.hour, now.minute, now.second, now.microsecond, filename)
    return url


# # ф-ция генерит путь для загружаемого изображения модели ImagesResidentialComplex
# def generate_url_for_imagerescomlex(self, filename):
#     ext = filename.split('.')[-1]
#     name = filename.split('.')[0]
#     filename = "%s.%s" % (slugify(self.residential_complex.name, to_lower=True), ext)
#     now = datetime.datetime.now()
#     url = 'images/realestate/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
#                                                        now.hour, now.minute, now.second, now.microsecond, filename)
#     return url


# ф-ция генерит путь для thumbnail image
def some_model_thumb_name(instance, filename):
    now = datetime.datetime.now()
    url = 'images/realestate/%s/%s/%s/%s' % (now.year, now.month, now.day, filename)
    return url


# ф-ция генерит путь для загружаемого планировок
def generate_url_for_floor_plan(self, filename):
    if hasattr(self, 'alt_attr') and self.alt_attr != '':
        name_file = self.alt_attr
    else:
        name_file = 'floor_plan_image'

    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    filename = "%s.%s" % (slugify(name_file, to_lower=True), ext)

    now = datetime.datetime.now()
    url = 'images/realestate/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                       now.hour, now.minute, now.second, now.microsecond, filename)
    return url


# ф-ция генерит путь для загружаемого логотипа застройщика
def generate_url_for_logo_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/logo_image/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                       now.hour, now.minute, now.second, now.microsecond, filename)
    return url


class Deadline(models.Model):
    """Модель Срок сдачи"""
    full_date = models.CharField(max_length=10, unique=True, verbose_name='Срок сдачи')
    only_year = models.IntegerField(db_index=True, verbose_name='Год срока сдачи')
    only_quarter = models.IntegerField(db_index=True, verbose_name='Квартал срока сдачи')

    def __str__(self):
        return self.full_date

    class Meta:
        verbose_name = 'Срок сдачи'
        verbose_name_plural = 'Сроки сдачи'
        # ordering = ['name']


class Developer(models.Model):
    """Модель Застройщик"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Застройщик')
    description = models.TextField(blank=True, verbose_name='Описание')
    logo_image = models.FileField(upload_to=generate_url_for_logo_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Логотип застройщика")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'
        ordering = ['name']


class ClassOfHousing(models.Model):
    """Модель Класс Жилья"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Класс Жилья')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс Жилья'
        verbose_name_plural = 'Классы Жилья'
        ordering = ['name']


class FloorInBuilding(models.Model):
    """Модель Этаж"""
    num_floor = models.IntegerField(db_index=True, verbose_name='Этаж')

    def __str__(self):
        return f'{self.num_floor}'

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'
        ordering = ['num_floor']


class NamesOfMetroStations(models.Model):
    """Модель Метро"""
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    distance_to_center = models.CharField(max_length=50, null=True, blank=True, verbose_name='Расстояние до центра')
    sub_text_distance_to_center = models.CharField(max_length=255, null=True, blank=True,
                                                   verbose_name='Текс для тултипа')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'
        ordering = ['name']


class MaterialWallsOfHouse(models.Model):
    """Модель Материал стен дома"""
    name = models.CharField(max_length=255, unique=True, verbose_name='Материал стен дома')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал стен дома'
        verbose_name_plural = 'Материалы стен дома'
        ordering = ['name']


class ApartmentDecoration(models.Model):
    """Модель Отделка квартиры"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделка квартиры'
        verbose_name_plural = 'Отделки квартиры'
        ordering = ['name']


class Infrastructure(models.Model):
    """Модель Инфраструктура"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    icon = models.FileField(upload_to=generate_url_for_image,
                            null=True,
                            blank=True,
                            verbose_name="Иконка")
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Инфраструктура'
        ordering = ['name']


class NumberOfRooms(models.Model):
    """Модель Количество комнат"""
    name = models.CharField(max_length=10, unique=True, verbose_name='Название')
    additional_name = models.CharField(max_length=150, blank=True, verbose_name='Добавочное название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Количество комнат'
        verbose_name_plural = 'Количество комнат'
        ordering = ['id']


class ResidentialComplex(models.Model):
    """Модель Жилого Комплекса"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')

    is_active_load_data = models.BooleanField(default=False, verbose_name='Включить загруженные данные о квартирах',
                                              help_text='Отключит данные о квартирах, занесенные вручную.')

    name = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Название ЖК')
    url_name = models.CharField(max_length=255, unique=True, verbose_name='URL для этого ЖК',
                                help_text='Для адресной строки в браузере. Только ЛАТИНИИЦА!!! Без: / и пробелов.')

    logo_image = models.FileField(upload_to=generate_url_for_logo_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Логотип ЖК")

    developer = models.ForeignKey(Developer,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Застройщик',
                                  related_name="rescomplex_developer",
                                  default=None,
                                  null=True,
                                  blank=True)
    class_of_housing = models.ForeignKey(ClassOfHousing,
                                         on_delete=models.SET_NULL,
                                         verbose_name='Класс Новостройки',
                                         related_name='rescomplex_classofhousing',
                                         default=None,
                                         null=True,
                                         blank=True)
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               verbose_name='Область',
                               related_name='rescomplex_region',
                               default=None,
                               null=True,
                               blank=True)
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             verbose_name='Город',
                             related_name='rescomplex_city',
                             default=None,
                             null=True,
                             blank=True)
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Район',
                                 related_name='rescomplex_district',
                                 default=None,
                                 null=True,
                                 blank=True)
    address = models.ManyToManyField(Address,
                                     verbose_name='Адрес',
                                     related_name='rescomplex_address',
                                     default=None,
                                     blank=True)

    one_or_many_buildings = models.BooleanField(default=False, verbose_name='В ЖК несколько строений')

    number_of_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность',
                                            help_text='ОСТАВИТЬ ПУСТЫМ! Если в ЖК несколько строений')

    min_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность min')
    max_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность max')

    house_completed = models.BooleanField(default=False, verbose_name='Дом сдан, Да/Нет')
    deadline = models.ManyToManyField(Deadline,
                                      verbose_name='Срок сдачи',
                                      related_name='rescomplex_deadline',
                                      default=None,
                                      blank=True)
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Главное изображение ЖК",
                                  help_text='После сохранения автоматически меняет высоту картинки на 500px.<br>'
                                            'Соотношение сторон сохраняеться.')
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    main_image_thumb = models.FileField(upload_to=generate_url_for_image,
                                        null=True,
                                        blank=True,
                                        verbose_name="Thumbnail image",
                                        help_text='МОЖНО НЕ ЗАПОЛНЯТЬ, генирируеться автоматически из '
                                                  '"Главное изображение ЖК" с высотой картинки 300px.<br>'
                                                  'Соотношение сторон сохраняеться.')

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(blank=True, verbose_name='Описание')

    distance_to_metro = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Растояние до метро, м')
    metro_stations = models.ManyToManyField(NamesOfMetroStations,
                                            verbose_name='Название ближайщего метро',
                                            related_name='rescomplex_metrostations',
                                            default=None,
                                            blank=True)

    site_developer = models.URLField(max_length=300,
                                     verbose_name='Сайт застройщика/Жилого комплекса',
                                     default=None,
                                     null=True,
                                     blank=True)

    infrastructure = models.ManyToManyField(Infrastructure,
                                            verbose_name='Инфраструктура',
                                            related_name='rescomplex_infrastructure',
                                            default=None,
                                            blank=True)
    material_walls = models.ManyToManyField(MaterialWallsOfHouse,
                                            verbose_name='Материал стен дома',
                                            related_name='rescomplex_materialwalls',
                                            default=None,
                                            blank=True)
    apart_decoration = models.ManyToManyField(ApartmentDecoration,
                                              verbose_name='Отделка',
                                              related_name='rescomplex_apartdecoration',
                                              default=None,
                                              blank=True)
    is_visible_video = models.BooleanField(default=False, verbose_name='Показывать видео')

    # создание миниатюр для "Главное изображение ЖК" будет происходить каждый раз при сохранении модели.
    # Постараемся с этим побороться, добавив в модель следующий метод:
    def __init__(self, *args, **kwargs):
        super(ResidentialComplex, self).__init__(*args, **kwargs)
        if self.main_image:
            self.__original_main_image = self.main_image.url
            self.__old_main_image = self.main_image.url
            self.__old_main_image_thumb = self.main_image_thumb

        else:
            # # else нужен чтоб не выскакивала ошибка AttributeError,
            # # когда создаётся новый объект и в него добовляются картинки,
            # # так как self.__original_main_image не существует
            self.__original_main_image = ''
            self.__old_main_image = ''
            self.__old_main_image_thumb = ''

    def __str__(self):
        return self.name

    # Путь до миниатюры "Главное изображение ЖК"
    def get_thumb_main_image_url(self):
        return settings.MEDIA_URL + self.main_image_thumb

    def save(self, *args, **kwargs):

        if self.main_image and hasattr(self.main_image, 'url') and self.main_image.url != self.__original_main_image:

            # print(self.__old_main_image)
            # print(self.__old_main_image_thumb)

            # size = {'height': 200, 'width': 320}

            super(ResidentialComplex, self).save(*args, **kwargs)
            extension = str(self.main_image.path).rsplit('.', 1)[1]  # получаем расширение загруженного файла
            # получаем имя загруженного файла (без пути к нему и расширения)
            filename = str(self.main_image.path).rsplit(os.sep, 1)[1].rsplit('.', 1)[0]
            # print(filename)
            # получаем путь к файлу (без имени и расширения)
            fullpath = str(self.main_image.path).rsplit(os.sep, 1)[0]
            # print(fullpath)

            if extension in ['jpg', 'jpeg', 'png']:  # если расширение входит в разрешенный список
                im = Image.open(str(self.main_image.path))  # открываем изображение

                # Это необходимо для сохранения вашего изображения в формате JPEG.
                if im.mode != 'RGB':
                    im = im.convert('RGB')

                (width, height) = im.size  # получаем width и height загружаемой картинки
                # print('width:', width)
                # print('height:', height)

                # Обработываем main_image
                new_height_main_image = 500
                new_width_main_image = int(new_height_main_image * width / height)
                im.thumbnail((new_width_main_image, new_height_main_image))
                resize_main_image = filename + "_" + str(new_width_main_image) + "x" + str(
                    new_height_main_image) + '.' + extension
                im.save(fullpath + os.sep + resize_main_image, 'JPEG', optimize=True, quality=60)
                self.main_image = some_model_thumb_name(self, resize_main_image)

                # Обработываем main_image_thumb
                new_height_thumb = 300  # Высота
                # Изменение высоты изображения, пропорционально обновляем и ширину
                new_width_thumb = int(new_height_thumb * width / height)
                im.thumbnail((new_width_thumb, new_height_thumb))

                # создаем миниатюру указанной ширины и высоты (важно - im.thumbnail сохраняет пропорции изображения!)
                # im.thumbnail((size['width'], size['height']))

                # имя нового изображения в формате oldname_60x60.jpg
                thumbname = filename + "_" + str(new_width_thumb) + "x" + str(new_height_thumb) + '.' + extension

                # сохраняем полученную миниатюру
                im.save(fullpath + os.sep + thumbname, 'JPEG', optimize=True, quality=60)

                # записываем путь к ней в поле image_thumb в модели
                self.main_image_thumb = some_model_thumb_name(self, thumbname)

                # Удаляем оригинал картинки
                # print(fullpath + filename + '.' + extension)
                if os.path.exists(str(fullpath + '/' + filename + '.' + extension)):
                    os.remove(str(fullpath + '/' + filename + '.' + extension))

                # Удаляем старую большую картинку
                if self.__old_main_image != '':
                    name = str(self.__old_main_image).rsplit('/', 1)[1]
                    if os.path.exists(str(fullpath + '/' + name)):
                        os.remove(str(fullpath + '/' + name))
                    #     print('delete')
                    # else:
                    #     print('not path', str(fullpath + '/' + name))

                # Удаляем старую маленькую картинку
                if self.__old_main_image_thumb != '':
                    name = str(self.__old_main_image_thumb).rsplit('/', 1)[1]
                    if os.path.exists(str(fullpath + '/' + name)):
                        os.remove(str(fullpath + '/' + name))
                    #     print('delete')
                    # else:
                    #     print('not path', str(fullpath + '/' + name))

                super(ResidentialComplex, self).save(*args, **kwargs)

        else:
            super(ResidentialComplex, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Жилой Комплекс'
        verbose_name_plural = 'Жилые Комплексы'
        ordering = ['id']


class ResidentialPremise(models.Model):
    """Модель Жилого помещения"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')
    res_complex = models.ForeignKey(ResidentialComplex,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Жилой комплекс',
                                    related_name='respremises_rescomplex',
                                    default=None,
                                    null=True,
                                    blank=True)
    number_rooms = models.ForeignKey(NumberOfRooms,
                                     on_delete=models.SET_NULL,
                                     verbose_name='Количество комнат',
                                     related_name='respremises_numberrooms',
                                     default=None,
                                     null=True)

    area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь')
    min_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь от, м')
    max_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь до, м')

    price = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Цена')
    min_price = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Цена от, м')
    max_price = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Цена до, м')

    floor = models.ManyToManyField(FloorInBuilding,
                                   verbose_name='Этаж',
                                   related_name='respremises_floor',
                                   default=None,
                                   blank=True)

    def __str__(self):
        return f'{self.res_complex} - {self.number_rooms}'

    class Meta:
        verbose_name = 'Жилое помещение'
        verbose_name_plural = 'Жилые помещения'
        # ordering = ['name']


class ImagesResidentialComplex(models.Model):
    """Модель Изображение Жилого Комплекса"""
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Изображение",
                             help_text='После сохранения автоматически меняет высоту картинки на 500px.<br>'
                                       'Соотношение сторон сохраняеться.'
                             )
    image_thumb = models.FileField(upload_to=generate_url_for_image,
                                   null=True,
                                   blank=True,
                                   verbose_name="Thumbnail image",
                                   help_text='МОЖНО НЕ ЗАПОЛНЯТЬ, генирируеться автоматически из '
                                             '"Главное изображение ЖК" с высотой картинки 300px.<br>'
                                             'Соотношение сторон сохраняеться.'
                                   )
    residential_complex = models.ForeignKey(ResidentialComplex,
                                            verbose_name="Жилой Комплекс",
                                            related_name='images_residential_complex',
                                            on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super(ImagesResidentialComplex, self).__init__(*args, **kwargs)
        if self.image:
            self.__original_image = self.image.url
            self.__old_image = self.image.url
            self.__old_image_thumb = self.image_thumb

        else:
            self.__original_image = ''
            self.__old_image = ''
            self.__old_image_thumb = ''

    def __str__(self):
        return f'{self.id}'

    def get_thumb_image_url(self):
        return settings.MEDIA_URL + self.image_thumb

    def save(self, *args, **kwargs):

        if self.image and hasattr(self.image, 'url') and self.image.url != self.__original_image:

            # size = {'height': 200, 'width': 320}

            super(ImagesResidentialComplex, self).save(*args, **kwargs)
            extension = str(self.image.path).rsplit('.', 1)[1]  # получаем расширение загруженного файла
            # получаем имя загруженного файла (без пути к нему и расширения)
            filename = str(self.image.path).rsplit(os.sep, 1)[1].rsplit('.', 1)[0]
            # получаем путь к файлу (без имени и расширения)
            fullpath = str(self.image.path).rsplit(os.sep, 1)[0]
            # print(str(self.main_image.path))

            if extension in ['jpg', 'jpeg', 'png']:  # если расширение входит в разрешенный список
                im = Image.open(str(self.image.path))  # открываем изображение

                if im.mode != 'RGB':
                    im = im.convert('RGB')

                (width, height) = im.size  # получаем width и height загружаемой картинки

                # Обработываем main_image
                new_height_image = 500
                new_width_image = int(new_height_image * width / height)
                im.thumbnail((new_width_image, new_height_image))
                resize_image = filename + "_" + str(new_width_image) + "x" + str(
                    new_height_image) + '.' + extension
                im.save(fullpath + os.sep + resize_image, 'JPEG', optimize=True, quality=60)
                self.image = some_model_thumb_name(self, resize_image)

                new_height_thumb = 300  # Высота
                new_width_thumb = int(new_height_thumb * width / height)
                im.thumbnail((new_width_thumb, new_height_thumb))
                thumbname = filename + "_" + str(new_width_thumb) + "x" + str(new_height_thumb) + '.' + extension
                im.save(fullpath + os.sep + thumbname, 'JPEG', optimize=True, quality=60)

                self.image_thumb = some_model_thumb_name(self, thumbname)

                if os.path.exists(str(fullpath + '/' + filename + '.' + extension)):
                    os.remove(str(fullpath + '/' + filename + '.' + extension))

                if self.__old_image != '':
                    name = str(self.__old_image).rsplit('/', 1)[1]
                    if os.path.exists(str(fullpath + '/' + name)):
                        os.remove(str(fullpath + '/' + name))

                if self.__old_image_thumb != '':
                    name = str(self.__old_image_thumb).rsplit('/', 1)[1]
                    if os.path.exists(str(fullpath + '/' + name)):
                        os.remove(str(fullpath + '/' + name))

                super(ImagesResidentialComplex, self).save(*args, **kwargs)

        else:
            super(ImagesResidentialComplex, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Изображение Жилого Комплекса"
        verbose_name_plural = "Изображения Жилого Комплекса"


class FloorPlansResidentialPremise(models.Model):
    """Модель Планировка Жилого помещения"""
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    image = models.FileField(upload_to=generate_url_for_floor_plan,
                             null=True,
                             blank=True,
                             verbose_name="Планировка Жилого помещения")

    residential_premises = models.ForeignKey(ResidentialPremise,
                                             verbose_name="Жилое помещение",
                                             related_name='floor_residential_premises',
                                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Планировка Жилого помещения"
        verbose_name_plural = "Планировки Жилого помещения"


class VideoResidentialComplex(models.Model):
    """Модель Видео Жилого Комплекса"""
    link_on_video = models.URLField(max_length=2000,
                                    verbose_name='Ссылка на видео',
                                    default=None,
                                    null=True,
                                    blank=True)
    residential_complex = models.ForeignKey(ResidentialComplex,
                                            verbose_name="Жилой Комплекс",
                                            related_name='video_residential_complex',
                                            on_delete=models.CASCADE)
    add_text = models.CharField(max_length=300, blank=True, verbose_name='Доплнительный текст')

    class Meta:
        verbose_name = 'Видео Жилого Комплекса'
        verbose_name_plural = 'Видео Жилого Комплекса'
        ordering = ['id']
