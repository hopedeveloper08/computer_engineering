from django.db import models
from django.contrib.auth.models import AbstractUser


class Trader(AbstractUser):
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    credit_card = models.IntegerField(null=True, blank=True)
    is_auth = models.BooleanField(default=False)

    def __str__(self):
        return self.username
