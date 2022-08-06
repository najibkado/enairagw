from django.urls import path
from .views.payment_gateway import PaymentIntentApiView

app_name = "api"

urlpatterns = [
    path('payment/intent', PaymentIntentApiView.as_view())
]