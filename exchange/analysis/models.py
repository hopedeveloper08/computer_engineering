from django.db import models


class Currency(models.Model):
    token = models.CharField(max_length=4, min_length=3, primary_key=True)
    name = models.CharField(max_length=32)
    price = models.FloatField()
    volume = models.FloatField()
    logo = models.ImageField()

    def __str__(self):
        return f"token: {self.token}"

    def show_chart(self) -> None:
        pass

    def show_news(self) -> dict:
        pass

    def get_stop_price(self) -> float:
        return self.price - (self.price * (1 / 100))

    def get_target_price(self) -> float:
        return self.price + (self.price * (2 / 100))

    def set_alarm(self, is_highered: bool, price: float) -> None:
        alarm = Alarm(
            token=self,
            price=price,
            is_highered=is_highered,
        )
        alarm.save()

    def get_detail(self) -> dict:
        detail = {
            "token": self.token,
            "name": self.name,
            "price": self.price,
            "volume": self.volume,
            "logo": self.logo,
        }
        return detail


class Alarm(models.Model):
    token = models.ForeignKey(Currency, on_delete=models.CASCADE)
    alarm_price = models.FloatField()
    is_highered = models.BooleanField()

    def __str__(self) -> str:
        return f"alarm: {self.alarm_price}"

    def check_alarm(self) -> bool:
        if self.is_highered and self.token.price >= self.alarm_price:
            return True

        if not self.is_highered and self.token.price <= self.alarm_price:
            return True

        return False
