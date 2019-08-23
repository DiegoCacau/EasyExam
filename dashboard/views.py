from django.http import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View

from .models import *



class LoginView(View):

    def get(self, request):
        if(request.user.is_authenticated):
            return HttpResponseRedirect(reverse("index"))
            

        return render(request, 'login.html')

    def post(self, request):
        try:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
            else:
                messages.error(request, "Login ou usuário incorretos.")
        except Exception as e:
            print(str(e))
            # messages.error(request, str(e))
        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

        return HttpResponseRedirect(reverse('index'))


class IndexView(View):

    def get(self, request):
        if(not request.user.is_authenticated):
            return HttpResponseRedirect(reverse("login"))
            
        return render(request, 'index.html')


class ConfigurationView(View):

    def get(self, request):
        if(not request.user.is_authenticated):
            return HttpResponseRedirect(reverse("login"))

        profile = Profile.objects.get(user=request.user)
            
        return render(request, 'configurations.html',
                      {"profile": profile})

    def post(self, request):
        messages.error(request, "Login ou usuário incorretos.")

        try:
            profile = Profile.objects.get(user=request.user)

            profile.name = request.POST["user_name"]
            profile.user.email = request.POST["email"]
            profile.receive_email = request.POST["pswitch"]

            profile.user.set_password(request.POST["pass"])

            profile.save()

            messages.success(request, "Configurações salvas com sucesso!")

        except Exception as e:
            messages.error(request, str(e))

        return render(request, 'configurations.html',
                      {"profile": profile})