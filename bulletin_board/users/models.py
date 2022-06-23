from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='accounts/image/%Y/%m/%d',blank=True,verbose_name='Аватар')
