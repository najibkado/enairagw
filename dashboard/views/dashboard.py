from lib2to3.pgen2 import token
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from dashboard.models import User, Wallet, Payment_Intent, PaymentAttempt
from rest_framework.authtoken.models import Token
import qrcode
import qrcode.image.svg
from io import BytesIO
from dashboard.adaptors import bvn
from django.urls import reverse

# Create your views here.
@login_required
def dashboard_view(request):
    # users = User.objects.all()
    # for usr in users:
    #     Wallet.objects.create(
    #         user=usr,
    #         balance=0.00
    #     )
    token = Token.objects.get(user=request.user)
    wallet = Wallet.objects.get(user=request.user)
    # transactions = Payment_Settlement.objects.filter(user=request.user)
    return render(request, "dashboard/dashboard.html", {
        "token": token,
        "balance": wallet.balance
    })

def error_view(request):
    return render(request, "payment/error.html")


def qr_view(request, id):
    #TODO: Use payment adaptor to generate payment link for the payment intent id 

    # try:
    #     intent = Payment_Intent.objects.get(pk=id)
    # except Payment_Intent.DoesNotExist:
    #     return HttpResponseRedirect(reverse("dashboard:error"))

    factory = qrcode.image.svg.SvgImage
    img = qrcode.make("https://tenaira.page.link/jbhj", image_factory=factory, box_size=20)
    stream = BytesIO()
    img.save(stream)

    return render(request, "payment/qr.html", {
        "svg": stream.getvalue().decode(),
        "id": id
    })

def payment_attempt_view(request, id):

    if request.method == "GET":
        intent = Payment_Intent.objects.get(pk=id)
        intent.status = "processed"
        intent.save()

        attempt = PaymentAttempt.objects.create(
            user = intent.user,
            payment_intent = intent,
            amount = intent.amount,
            status = "success",
            added = False
        )

        attempt.save()

        merchant_wallet = Wallet.objects.get(user=intent.user)
        merchant_wallet.balance += attempt.amount
        merchant_wallet.save()

        attempt.added = True
        attempt.save()

        return HttpResponseRedirect(intent.return_url)
