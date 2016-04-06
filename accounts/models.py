from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField()

    @property
    def initials(self):
        return '{}'.format(self.first_name[0], self.last_name[0])


class NotificationSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    disable_all = models.BooleanField(default=False)
