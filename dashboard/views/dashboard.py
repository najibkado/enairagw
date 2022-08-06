from lib2to3.pgen2 import token
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import User, Wallet
from rest_framework.authtoken.models import Token
import qrcode
import qrcode.image.svg
from io import BytesIO
from dashboard.adaptors import bvn

# Create your views here.
@login_required
def dashboard_view(request):
    # bv = bvn.Bvn("22227412134")
    # bv.verify()
    token = Token.objects.get(user=request.user)
    wallet = Wallet.objects.get(user=request.user)
    # transactions = Payment_Settlement.objects.filter(user=request.user)
    return render(request, "dashboard/dashboard.html", {
        "token": token,
        "balance": wallet.balance
    })


def qr_view(request, id):
    #TODO: Use payment adaptor to generate payment link for the payment intent id 
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make("https://tenaira.page.link/jbhj", image_factory=factory, box_size=20)
    stream = BytesIO()
    img.save(stream)

    return render(request, "payment/qr.html", {
        "svg": stream.getvalue().decode()
    })