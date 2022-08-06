from django.db import models
from django.contrib.auth.models import AbstractUser
# from api.models import Payment_Intent

class User(AbstractUser):
    bvn = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    tin = models.CharField(max_length=255)

class Wallet(models.Model):
    """
    This module stores the merchant wallet details locally for easy access
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wallet")
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

class PaymentAttempt(models.Model):
    """
    Transactions created by merchant to satisfy a given order
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment")
    # payment_intent = models.ForeignKey(Payment_Intent, on_delete=models.CASCADE, related_name="attempt")
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=255)
    added = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

class PaymentSettlement(models.Model):
    """
    A set of payment paid to a merchant in a single batch
    """
    pass


