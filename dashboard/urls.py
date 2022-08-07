from django.urls import path
from .views import (
    dashboard, 
    auth,
    )

app_name = "dashboard"

urlpatterns = [
    path('', dashboard.dashboard_view, name="dashboard"),
    path('login', auth.login_view, name="login"),
    path('register', auth.register_view, name="register"),
    path('logout', auth.logout_view, name="logout"),
    path('qr/<int:id>', dashboard.qr_view, name="qr"),
    path('error', dashboard.error_view, name="error"),
    path('confirmpay/<int:id>', dashboard.payment_attempt_view, name="attempt")
]