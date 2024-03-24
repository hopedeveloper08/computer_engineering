from datetime import datetime
from django.db import models


class Trader(models.Model):
    LEVELS = (
        ('G', "Guest"),
        ('H', "Holder"),
        ('T', "Trader"),
    )

    national_id = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(primary_key=True)
    account_number = models.DecimalField(max_digits=16)
    subscription_time = models.DateTimeField()
    level = models.CharField(max_length=1, choices=LEVELS, default='G')

    def __str__(self) -> str:
        return f"username: {self.username}"

    def level_up(self, new_level: str) -> None:
        self.level = new_level
        self.save()

    def authentication(self, account_number: str) -> None:
        if not self.is_authenticated() and account_number:
            self.account_number = account_number
            self.level_up('H')
            self.save()

    def is_authenticated(self) -> bool:
        if self.level == 'G':
            return False

        return True

    def subscription_up(self, new_datetime: datetime) -> None:
        if self.is_authenticated():
            self.subscription_time = new_datetime
            self.level_up('T')
            self.save()
