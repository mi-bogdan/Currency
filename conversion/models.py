
from django.db import models


class Valute(models.Model):
    from_amount = models.IntegerField(verbose_name="Число", )
    from_curr = models.CharField(verbose_name="из_какой_вылюты", max_length=10)
    to_curr = models.CharField(verbose_name="в_какую_валюту", max_length=10)
    converted_amount = models.FloatField(verbose_name="Сумма")
    data_converted = models.DateTimeField(
        verbose_name="Дата операции", auto_now_add=True)

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"
