import imp
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib import messages
from dashboard.models import User, Wallet
from django.db import IntegrityError
from rest_framework.authtoken.models import Token

def login_view(request):

    if request.method == "GET":
        return render(request, "auth/login.html")

    if request.method == "POST":
        
        #Get user data
        username = request.POST["username"]
        password = request.POST["password"]

        #Verify user data
        if username == "" or password == "":

            #Return an error message if not verified
            messages.error(request, "Enter username and password")
            return HttpResponseRedirect(reverse("dashboard:login"))

         #Authenticate user
        authenticated_user = authenticate(request, username=username, password=password)

        #Verify authenticated user
        if authenticated_user is not None:
            
            #login user
            login(request, authenticated_user)

            #Redirect user to dashboard
            return HttpResponseRedirect(reverse("dashboard:dashboard"))

        else:

            #Return an error message if not verified
            messages.error(request, "Invalid user credentials")
            return HttpResponseRedirect(reverse("dashboard:login"))


def register_view(request):

    if request.method == "GET":
        return render(request, "auth/register.html")

     #Handle POST request
    if request.method == "POST":

        #Collect User Data
        name = request.POST["name"]
        bvn = request.POST["bvn"] #BVN
        email = request.POST["email"]
        password = request.POST["password"]
        bank = request.POST["bank"] #eNaira alias
        account = request.POST["account"] #eNaira alias business name
        tin = request.POST["tin"] #BVN Name

        #Verify User Data
        if name == "" or bvn == "" or email == "" or password == "" or bank == "" or account == "" or tin == "":
            messages.error(request, "Fields can't be empty")
            return HttpResponseRedirect(reverse("dashboard:register"))

        #Verify Password Length
        if len(password) < 6:
            messages.error(request, "Password too short")
            return HttpResponseRedirect(reverse("dashboard:register"))

        #Verify Account number
        # if len(account) < 10 or len(account) > 10:
        #     messages.error(request, "Invalid Account Number")
        #     return HttpResponseRedirect(reverse("dashboard:register"))

        #Ensure User Email Does not Exist
        if User.objects.filter(email=email).exists():

            messages.error(request, "Unable to create account, please try again")
            return HttpResponseRedirect(reverse("dashboard:register"))

        elif User.objects.filter(username=email).exists():
            
            messages.error(request, "Unable to create account, please try again")
            return HttpResponseRedirect(reverse("dashboard:register"))

        else:
            #Create New User
            try:
                new_user = User.objects.create_user(
                    first_name = name,
                    bvn = bvn,
                    bank = bank,
                    account = account,
                    tin = tin,
                    username = email,
                    email = email,
                    password = password
                )
                new_user.save()

                new_wallet = Wallet.objects.create(
                    user=new_user,
                    balance=0.00
                )

                new_wallet.save()
            except IntegrityError:
                messages.error(request, "Unable to create account, please try again")
                return HttpResponseRedirect(reverse("dashboard:register"))
            
            token = Token.objects.create(user=new_user)

            #Login User
            login(request, new_user)

            #Redirect User To Dashboard

            return HttpResponseRedirect(reverse("dashboard:dashboard"))


@login_required
def logout_view(request):
    
    logout(request)
    return HttpResponseRedirect(reverse("dashboard:login"))