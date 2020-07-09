from django.db import models
from django.contrib.auth import get_user_model

import os
import datetime
from slugify import slugify  # тут используется awesome-slugify
from PIL import Image  # для обработки изображения нам нужен pillow

from project import settings
from geo_location.models import Region, City, District, Address
from residential_real_estate.models import FloorInBuilding, ResidentialComplex, NamesOfMetroStations

User = settings.AUTH_USER_MODEL


def generate_url_for_image(self, filename):
    # проверяет в какой model была фызвана ф-ция, и бирёт нужный атрибут для имени файла
    if hasattr(self, 'name'):
        name_file = self.name
    # elif hasattr(self, 'residential_complex'):
    #     name_file = self.residential_complex.name
    elif hasattr(self, 'alt_attr') and self.alt_attr != '':
        name_file = self.alt_attr
    else:
        name_file = 'commerce_estate_image'

    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    filename = "%s.%s" % (slugify(name_file, to_lower=True), ext)
    now = datetime.datetime.now()
    url = 'images/realestate/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                       now.hour, now.minute, now.second, now.microsecond, filename)
    return url


# ф-ция генерит путь для thumbnail image
def some_model_thumb_name(instance, filename):
    now = datetime.datetime.now()
    url = 'images/realestate/%s/%s/%s/%s' % (now.year, now.month, now.day, filename)
    return url


class BusinessCategory(models.Model):
    """Модель Категория бизнеса"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория бизнеса'
        verbose_name_plural = 'Категории бизнесов'
        ordering = ['name']


class TypeCommercialEstate(models.Model):
    """Модель Тип коммерческой недвижимости"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип коммерческой недвижимости'
        verbose_name_plural = 'Типы коммерческой недвижимости'
        ordering = ['name']


class CookerHood(models.Model):
    """Модель Вытяжка"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вытяжка'
        verbose_name_plural = 'Вытяжки'
        ordering = ['name']


class TypeEntranceToCommercialEstate(models.Model):
    """Модель Тип входа в коммерческое помещение"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип входа в коммерческое помещение'
        verbose_name_plural = 'Типы входов в коммерческое помещение'
        ordering = ['name']


class CommunicationSystems(models.Model):
    """Модель Системы коммуникаций"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Системы коммуникаций'
        verbose_name_plural = 'Системы коммуникаций'
        ordering = ['name']


class RelativeLocation(models.Model):
    """Модель Расположение, линия"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположения'
        ordering = ['name']


class FinishingProperty(models.Model):
    """Модель Отделка коммерческой недвижимости"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделка коммерческой недвижимости'
        verbose_name_plural = 'Отделки коммерческой недвижимости'
        ordering = ['name']


class PurchaseMethod(models.Model):
    """Модель Способы покупки"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Способ покупки'
        verbose_name_plural = 'Способы покупки'
        ordering = ['name']


class BusinessCenter(models.Model):
    """Модель Бизнес центр"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бизнес центр'
        verbose_name_plural = 'Бизнес центры'
        ordering = ['name']


class CommercialEstate(models.Model):
    """Модель Коммерческого помещения"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать')

    is_group_multiple_objs = models.BooleanField(default=False, verbose_name='Сгруппировать несколько объектов',
                                                 help_text='Если нужно занести несколько помещений в одну карточку.')

    use_contacts_fixed_agent = models.BooleanField(default=False,
                                                   verbose_name='Использовать контакты Закреплённого(-ых) агента(-ов)')
    fixed_agent = models.ManyToManyField(User,
                                         verbose_name='Закреплённый агент',
                                         related_name='comestate_fixedagent',
                                         default=None,
                                         blank=True)

    cost_service = models.FloatField(null=True, blank=True, verbose_name='Стоимость услуг')

    is_sale = models.BooleanField(default=False, verbose_name='Продажа')
    is_rent = models.BooleanField(default=False, verbose_name='Аренда')

    area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь')
    min_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь от, м')
    max_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь до, м')

    ground_floor = models.BooleanField(default=False, verbose_name='Цоколь')
    basement = models.BooleanField(default=False, verbose_name='Подвал')
    floor = models.ManyToManyField(FloorInBuilding,
                                   verbose_name='Этаж',
                                   related_name='comestate_floor',
                                   default=None,
                                   blank=True)
    number_of_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность здания')

    several_floors = models.BooleanField(default=False, verbose_name='Недвижимость с несколькими этажами')

    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               verbose_name='Область',
                               related_name='comestate_region',
                               default=None,
                               null=True,
                               blank=True)
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             verbose_name='Город',
                             related_name='comestate_city',
                             default=None,
                             null=True,
                             blank=True)
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Район',
                                 related_name='comestate_district',
                                 default=None,
                                 null=True,
                                 blank=True)
    # address = models.CharField(max_length=150, default=None, blank=True, verbose_name='Адрес')
    address = models.ForeignKey(Address,
                                on_delete=models.SET_NULL,
                                verbose_name='Адрес',
                                related_name='comestate_address',
                                default=None,
                                null=True,
                                blank=False)

    distance_to_metro = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Растояние до метро, м')
    metro_stations = models.ManyToManyField(NamesOfMetroStations,
                                            verbose_name='Название ближайщего метро',
                                            related_name='comestate_metrostations',
                                            default=None,
                                            blank=True)

    relative_location = models.ManyToManyField(RelativeLocation,
                                               verbose_name='Расположение, линия',
                                               related_name='comestate_relativelocation',
                                               default=None,
                                               blank=True)

    business_center = models.ForeignKey(BusinessCenter,
                                        on_delete=models.SET_NULL,
                                        verbose_name='Бизнес центр',
                                        related_name='comestate_buscenter',
                                        default=None,
                                        null=True,
                                        blank=True)

    residential_complex = models.ForeignKey(ResidentialComplex,
                                            on_delete=models.SET_NULL,
                                            verbose_name='Жилой комплекс',
                                            related_name='comestate_rescomplex',
                                            default=None,
                                            null=True,
                                            blank=True)

    building_commercial_estate = models.BooleanField(default=False, verbose_name='Строящее',
                                                     help_text='Находиться в процессе строительства.')

    finished_commercial_estate = models.BooleanField(default=False, verbose_name='Готовое',
                                                     help_text='Построенное помещение.')

    type_commercial_estate = models.ManyToManyField(TypeCommercialEstate,
                                                    verbose_name='Тип коммерческой недвижимости',
                                                    related_name='comestate_purpose',
                                                    default=None,
                                                    blank=True)
    business_category = models.ManyToManyField(BusinessCategory,
                                               verbose_name='Категория бизнеса',
                                               related_name='comestate_businesscategory',
                                               default=None,
                                               blank=True)
    purchase_method = models.ManyToManyField(PurchaseMethod,
                                             verbose_name='Способы покупки',
                                             related_name='comestate_purchasemethod',
                                             default=None,
                                             blank=True)

    rent_price_sq_m = models.IntegerField(db_index=True, null=True, blank=True,
                                          verbose_name='Стоимость аренды, руб/кв.м.')
    rent_price_month = models.IntegerField(db_index=True, null=True, blank=True,
                                           verbose_name='Стоимость аренды, руб/мес.')

    cost_of_sale = models.IntegerField(db_index=True, null=True, blank=True,
                                       verbose_name='Стоймость на продажу')
    min_cost_of_sale = models.IntegerField(db_index=True, null=True, blank=True,
                                           verbose_name='Стоймость на продажу, от')
    max_cost_of_sale = models.IntegerField(db_index=True, null=True, blank=True,
                                           verbose_name='Стоймость на продажу, до')

    min_payback = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Окупаемость от, мес')
    max_payback = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Окупаемость до, мес')
    min_average_rental_rate = models.IntegerField(db_index=True, null=True, blank=True,
                                                  verbose_name='Средняя арендная ставка от, руб/кв.м.')
    max_average_rental_rate = models.IntegerField(db_index=True, null=True, blank=True,
                                                  verbose_name='Средняя арендная ставка до, руб/кв.м.')
    possible_income = models.IntegerField(db_index=True, null=True, blank=True,
                                          verbose_name='Возможный доход, руб/мес.')

    year_construction = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Год постройки')
    finishing_property = models.ManyToManyField(FinishingProperty,
                                                verbose_name='Отделка',
                                                related_name='comestate_finproperty',
                                                default=None,
                                                blank=True)

    kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт')
    min_kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт, от')
    max_kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт, до')
    comment_kw = models.CharField(max_length=255, blank=True,
                                  verbose_name='Комментарий к "кВт"')

    ceiling_height = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Высота потолков, м.')
    min_ceiling_height = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Высота потолков от, м.')
    max_ceiling_height = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Высота потолков до, м.')
    comment_ceiling_height = models.CharField(max_length=255, blank=True,
                                              verbose_name='Комментарий к "Высота потолков"')

    communication_systems = models.ManyToManyField(CommunicationSystems,
                                                   verbose_name='Системы коммуникаций',
                                                   related_name='comestate_comsystems',
                                                   default=None,
                                                   blank=True)
    cooker_hood = models.ManyToManyField(CookerHood,
                                         verbose_name='Вытяжка',
                                         related_name='comestate_cookerhood',
                                         default=None,
                                         blank=True)
    type_entrance = models.ManyToManyField(TypeEntranceToCommercialEstate,
                                           verbose_name='Тип входа',
                                           related_name='comestate_typeentrance',
                                           default=None,
                                           blank=True)

    parking = models.BooleanField(default=False, verbose_name='Наличие парковки')
    min_parking = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Парковка от, шт.')
    max_parking = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Парковка до, шт.')
    comment_parking = models.CharField(max_length=255, blank=True,
                                       verbose_name='Комментарий к "Парковка"')

    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Главное изображение",
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

    def __init__(self, *args, **kwargs):
        super(CommercialEstate, self).__init__(*args, **kwargs)
        if self.main_image:
            self.__original_main_image = self.main_image.url
            self.__old_main_image = self.main_image.url
            self.__old_main_image_thumb = self.main_image_thumb

        else:
            self.__original_main_image = ''
            self.__old_main_image = ''
            self.__old_main_image_thumb = ''

    def __str__(self):
        return f'{self.address}'

    def get_thumb_main_image_url(self):
        return settings.MEDIA_URL + self.main_image_thumb

    def save(self, *args, **kwargs):

        if self.main_image and hasattr(self.main_image, 'url') and self.main_image.url != self.__original_main_image:
            super(CommercialEstate, self).save(*args, **kwargs)
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

                super(CommercialEstate, self).save(*args, **kwargs)

        else:
            super(CommercialEstate, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Коммерческая недвижимость'
        verbose_name_plural = 'Коммерческие недвижимости'
        # ordering = ['name']


class ImagesCommercialEstate(models.Model):
    """Модель Изображение Коммерческого помещения"""
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Изображение",
                             help_text='После сохранения автоматически меняет высоту картинки на 500px.<br>'
                                       'Соотношение сторон сохраняеться.')
    image_thumb = models.FileField(upload_to=generate_url_for_image,
                                   null=True,
                                   blank=True,
                                   verbose_name="Thumbnail image",
                                   help_text='МОЖНО НЕ ЗАПОЛНЯТЬ, генирируеться автоматически из '
                                             '"Главное изображение ЖК" с высотой картинки 300px.<br>'
                                             'Соотношение сторон сохраняеться.'
                                   )
    commercial_estate = models.ForeignKey(CommercialEstate,
                                          verbose_name="Коммерческая недвижимость",
                                          related_name='images_commercial_estate',
                                          on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super(ImagesCommercialEstate, self).__init__(*args, **kwargs)
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
            super(ImagesCommercialEstate, self).save(*args, **kwargs)
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

                super(ImagesCommercialEstate, self).save(*args, **kwargs)

        else:
            super(ImagesCommercialEstate, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Изображение Коммерческой недвижимости"
        verbose_name_plural = "Изображения Коммерческой недвижимости"


class FloorPlansCommercialEstate(models.Model):
    """Модель Планировка Коммерческого помещения"""
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Изображение",
                             help_text='После сохранения автоматически меняет высоту картинки на 500px.<br>'
                                       'Соотношение сторон сохраняеться.')
    image_thumb = models.FileField(upload_to=generate_url_for_image,
                                   null=True,
                                   blank=True,
                                   verbose_name="Thumbnail image",
                                   help_text='МОЖНО НЕ ЗАПОЛНЯТЬ, генирируеться автоматически из '
                                             '"Главное изображение ЖК" с высотой картинки 300px.<br>'
                                             'Соотношение сторон сохраняеться.'
                                   )
    commercial_estate = models.ForeignKey(CommercialEstate,
                                          verbose_name="Коммерческая недвижимость",
                                          related_name='floorplans_commercial_estate',
                                          on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super(FloorPlansCommercialEstate, self).__init__(*args, **kwargs)
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
            super(FloorPlansCommercialEstate, self).save(*args, **kwargs)
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

                super(FloorPlansCommercialEstate, self).save(*args, **kwargs)

        else:
            super(FloorPlansCommercialEstate, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Планировка Коммерческой недвижимости"
        verbose_name_plural = "Планировки Коммерческой недвижимости"


class VideoCommercialEstate(models.Model):
    """Модель Видео Коммерческого помещения"""
    link_on_video = models.URLField(max_length=2000,
                                    verbose_name='Ссылка на видео',
                                    default=None,
                                    null=True,
                                    blank=True)
    commercial_estate = models.ForeignKey(CommercialEstate,
                                          verbose_name="Коммерческая недвижимость",
                                          related_name='video_commercial_estate',
                                          on_delete=models.CASCADE)
    add_text = models.CharField(max_length=300, blank=True, verbose_name='Доплнительный текст')

    class Meta:
        verbose_name = 'Видео Коммерческого помещения'
        verbose_name_plural = 'Видео Коммерческого помещения'
        ordering = ['id']
