from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.apps import apps
from django.contrib.auth.hashers import make_password
# Create your models here.
"""Create a Book class with the following fields:
title: CharField with a maximum length of 200 characters.
author: CharField with a maximum length of 100 characters.
publication_year: IntegerField."""

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, date_of_birth, profile_photo, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, username, email=None, password=None, date_of_birth=None , profile_photo=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password,  date_of_birth, profile_photo, **extra_fields)

    def create_superuser(self, username, email=None, password=None, date_of_birth=None , profile_photo=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password,  date_of_birth, profile_photo, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    objects = CustomUserManager()