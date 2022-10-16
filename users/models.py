from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ('is_special', 'Special User Status'),
            ('is_regular', 'Regular User Status')
        ]