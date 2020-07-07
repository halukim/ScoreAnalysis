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


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    productNote = models.CharField(max_length=100)
    productModel = models.CharField(max_length=100)
    productCode = models.CharField(max_length=100)
    productUm = models.CharField(max_length=100)
    productBrand = models.CharField(max_length=100)
    productCategory = models.CharField(max_length=100)
    productColor = models.CharField(max_length=100)
    productSize = models.CharField(max_length=100)
    productCost = models.CharField(max_length=100)
    productPrice = models.CharField(max_length=100)
    productImgUrl1 = models.CharField(max_length=200)
    productImgUrl2 = models.CharField(max_length=200)

