from django.db import models
from account.models import Trader
from analysis.models import Currency


class Order(models.Model):
    token = models.ForeignKey(Currency, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    price = models.FloatField()
    amount = models.FloatField()
    is_buy = models.BooleanField()
    balance = models.FloatField(null=True, blank=True)
    is_confirm = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"balance: {self.balance}"

    def set_balance(self) -> None:
        self.balance = self.price * self.amount
        self.save()

    def apply_fee(self) -> None:
        if self.is_buy:
            self.price -= (self.price * (0.2 / 100))
        else:
            self.price += (self.price * (0.2 / 100))

        self.save()

    def confirm(self) -> None:
        self.is_confirm = True
        self.save()

    def get_details(self) -> dict:
        return {
            "id": self.id,
            "token": self.token,
            "create_at": self.create_at,
            "price": self.price,
            "amount": self.amount,
            "is_buy": self.is_buy,
            "balance": self.balance,
            "is_confirm": self.is_confirm,
        }
