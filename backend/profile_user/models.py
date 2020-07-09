from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group
# from django.utils.text import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.safestring import mark_safe

import os
import datetime
from slugify import slugify  # тут используется awesome-slugify
from PIL import Image  # для обработки изображения нам нужен pillow

from project import settings
from .managers import UserManager


def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])


# ф-ция генерит путь для загружаемого изображения
def generate_url_for_image(self, filename):
    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    filename = "%s.%s" % (slugify(name, to_lower=True), ext)
    now = datetime.datetime.now()
    url = 'images/users/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                  now.hour, now.minute, now.second, now.microsecond, filename)
    return url


# ф-ция генерит путь для thumbnail image
def some_model_thumb_name(instance, filename):
    now = datetime.datetime.now()
    url = 'images/users/%s/%s/%s/%s' % (now.year, now.month, now.day, filename)
    return url


class Specialization(models.Model):
    """Модель Специализация"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    short_name = models.CharField(max_length=10, unique=True, default=None, verbose_name='Короткое название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'
        ordering = ['name']


class JobTitle(models.Model):
    """Модель Должность"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    short_name = models.CharField(max_length=10, unique=True, default=None, verbose_name='Короткое название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name']


class User(AbstractBaseUser, PermissionsMixin):
    """Модель Профиль юзера"""

    username = None
    email = models.EmailField(max_length=255, unique=True, verbose_name=_('email address'))
    password = models.CharField(max_length=128, verbose_name='Пароль')
    full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='ФИО')

    phone_number = models.CharField(max_length=20, blank=True, verbose_name='Телефон',
                                    help_text='Без пробелов, скобок, +7 и 8. '
                                              '<b style="color:red;font-size:10px;">ТОЛЬКО ЦИФРЫ !!!</b><br>'
                                              'Пример: 9131112233')
    job_title = models.ManyToManyField(JobTitle,
                                       verbose_name='Должность',
                                       related_name='user_jobtitle',
                                       default=None,
                                       blank=True)
    specialization = models.ManyToManyField(Specialization,
                                            verbose_name='Специализация',
                                            related_name='user_specialization',
                                            default=None,
                                            blank=True)
    GENDER_CHOICES = (
        ('female', 'Женский'),
        ('male', 'Мужской'),
    )
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=25,
                              blank=True,
                              verbose_name='Пол')
    birth_date = models.DateField(null=True, blank=True, verbose_name='День рождения',
                                  help_text='Формат: YYYY-MM-DD')
    bio = models.TextField(blank=True, verbose_name='О себе')
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Фото",
                             help_text='После сохранения автоматически меняет высоту картинки на 500px.<br>'
                                       'Соотношение сторон сохраняеться.'
                             )
    image_thumb = models.FileField(upload_to=generate_url_for_image,
                                   null=True,
                                   blank=True,
                                   verbose_name="Thumbnail Фото",
                                   help_text='<b style="color:red;font-size:10px;">МОЖНО НЕ ЗАПОЛНЯТЬ, '
                                             'генирируеться автоматически</b> из '
                                             '"Фото" с высотой картинки 300px.<br>'
                                             'Соотношение сторон сохраняеться.'
                                   )

    is_active = models.BooleanField(_('active'),
                                    default=True,
                                    help_text=_(
                                        'Designates whether this user should be treated as active. '
                                        'Unselect this instead of deleting accounts.'
                                    ))
    is_staff = models.BooleanField(_('staff status'),
                                   default=False,
                                   help_text=_(
                                       'Designates whether the user can log into this admin site.'
                                   ))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    update_date = models.DateTimeField(verbose_name=_('date update'),
                                       auto_now=True)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    USERNAME_FIELD = 'email'  # username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = []  # ['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        if self.full_name is not None and self.full_name != '':
            return f'{self.email} {self.full_name}'
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if self.image:
            self.__original_image = self.image.url
            self.__old_image = self.image.url
            self.__old_image_thumb = self.image_thumb

        else:
            self.__original_image = ''
            self.__old_image = ''
            self.__old_image_thumb = ''

    def get_thumb_image_url(self):
        return settings.MEDIA_URL + self.image_thumb

    def save(self, *args, **kwargs):

        if self.image and hasattr(self.image, 'url') and self.image.url != self.__original_image:

            # size = {'height': 200, 'width': 320}

            super(User, self).save(*args, **kwargs)
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

                super(User, self).save(*args, **kwargs)

        else:
            super(User, self).save(*args, **kwargs)


class SocialNetwork(models.Model):
    """Модель Социальная сеть"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    SOCNET_CHOICES = (
        ('whatsapp', 'Whatsapp'),
        ('telegram', 'Telegram'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('vk', 'VK'),
        ('twitter', 'Twitter'),
    )
    name = models.CharField(choices=SOCNET_CHOICES, max_length=25, blank=True,
                            verbose_name='Социальная сеть')
    link_on_socnet = models.URLField(max_length=2000,
                                     verbose_name='Ссылка',
                                     default=None,
                                     null=True,
                                     blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
        ordering = ['name']
