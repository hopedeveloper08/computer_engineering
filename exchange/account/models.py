from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout


class Trader(AbstractUser):
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    credit_card = models.IntegerField(null=True, blank=True)
    is_auth = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def register(self, username, password):
        try:
            self.username = username
            self.set_password(password)
            self.save()
        except Exception:
            return False

    @staticmethod
    def login(request, username, password):
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return True
        else:
            return False

    @staticmethod
    def logout(request):
        logout(request)

    def authenticate_user(self, phone_number, credit_card):
        self.phone_number = phone_number
        self.credit_card = credit_card
        self.is_auth = True
        self.save()
