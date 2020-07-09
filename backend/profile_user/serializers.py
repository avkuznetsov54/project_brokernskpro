from django.db import IntegrityError, transaction

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

from project import settings
from .models import User


class UserRegistrationSerializer(BaseUserRegistrationSerializer):

    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'email', 'password')

    # переопределяем метод, так как username поменяли на email
    def create(self, validated_data):
        try:

            email = self.perform_create(validated_data)

        except IntegrityError:
            self.fail("cannot_create_user")

        return email

    # переопределяем метод, добавили путь до переменной settings.DJOSER['SEND_ACTIVATION_EMAIL']
    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if settings.DJOSER['SEND_ACTIVATION_EMAIL']:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user
