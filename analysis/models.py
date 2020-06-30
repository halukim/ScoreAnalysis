from django.db import models


class Ticker(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=20)
    start_date = models.DateField()
    time_scale = models.IntegerField()
    open_price = models.FloatField
    status = models.IntegerField()


class TickerDate(models.Model):
    id = models.IntegerField(primary_key=True)
    ticker_date = models.CharField(max_length=10)
