from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class ClientManager(BaseUserManager):
    def _create_user(self, first_name, last_name, email, password, is_staff, is_superuser,
                     **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()

        if not email:
            raise ValueError('Email is Required!')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email,
                          is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        return self._create_user(first_name, last_name, email, password, False, False, **extra_fields)

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        return self._create_user(first_name, last_name, email, password, True, True, **extra_fields)
