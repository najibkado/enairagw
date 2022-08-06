from django.db import models
from dashboard.models import User

# Create your models here.
class Payment_Intent(models.Model):
    """
    Orders created by merchant to specify amount, products, customers, etc 
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="merchant")
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    order_id = models.CharField(max_length=255)
    return_url = models.CharField(max_length=255)
    redirect_url = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
