from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=False, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password)  # change user password
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        return user
