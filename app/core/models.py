from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email), **extra_fields
        )  # creates a new user model (a row?)
        user.set_password(password)
        user.save(using=self._db)  # works for when we have several databases

        return user

    def create_superuser(self, email, password):
        """Creates and saves new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instad of username"""

    email = models.EmailField(
        max_length=255, unique=True
    )  # you can only create one user with one email
    name = models.CharField(max_length=255)
    is_active = models.BooleanField
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"  # customizing