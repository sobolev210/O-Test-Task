from decimal import Decimal

from django.db import models


class Wallet(models.Model):
    CURRENCY_CHOICES = [
        ("ETH", "Ethereum")
    ]
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    public_key = models.CharField(max_length=255)
    private_key = models.JSONField()
    balance = models.DecimalField(max_digits=30, decimal_places=18, default=Decimal(0))  # 1 wei = 1E-18 ether
