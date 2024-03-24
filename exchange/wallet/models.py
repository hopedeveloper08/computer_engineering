from django.db import models
from account.models import Trader
from analysis.models import Currency


class Asset(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.FloatField()
    balance = models.FloatField()
    is_lock = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.currency.token}: {self.balance}'

    def update_balance(self) -> None:
        self.balance = self.currency.price * self.amount
        self.save()

    def deposit(self, amount: float) -> bool:
        if not self.trader.is_authenticated():
            return False

        self.amount += amount
        self.save()
        return True

    def withdraw(self, amount: float) -> bool:
        if not self.trader.is_authenticated() or amount > self.amount:
            return False

        self.amount -= amount
        self.amount = 0 if self.amount < 0 else self.amount

        self.save()
        return True

    def lock(self) -> None:
        self.is_lock = True
        self.save()

    def unlock(self) -> None:
        self.is_lock = False
        self.save()

    def get_all_currencies(self) -> models.QuerySet:
        currencies = self.trader.asset_set.all()
        return currencies
