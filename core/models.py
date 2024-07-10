from django.db import models

class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    long_name = models.CharField(max_length=100)
    regular_market_price = models.FloatField()
    regular_market_volume = models.IntegerField()
    regular_market_time = models.DateTimeField()

    def __str__(self):
        return self.symbol
