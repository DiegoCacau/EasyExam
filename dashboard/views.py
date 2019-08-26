from django.http import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import render

import datetime

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
            
        profile = Profile.objects.get(user=request.user)

        return render(request, 'index.html',
                      {"profile": profile})


class ConfigurationView(View):

    def get(self, request):
        if(not request.user.is_authenticated):
            return HttpResponseRedirect(reverse("login"))

        profile = Profile.objects.get(user=request.user)
            
        return render(request, 'configurations.html',
                      {"profile": profile})

    def post(self, request):

        if(not request.user.is_authenticated):
            return HttpResponseRedirect(reverse("login"))

        try:
            profile = Profile.objects.get(user=request.user)

            receive_email = False
            if(request.POST["receive_email"] == "1"):
                receive_email = True


            profile.name = request.POST["user_name"]
            profile.user.email = request.POST["email"]
            profile.receive_email = receive_email

            profile.save()

            messages.success(request, "Configurações salvas com sucesso!")

        except Exception as e:
            messages.error(request, str(e))

        return render(request, 'configurations.html',
                      {"profile": profile})


class NewPatientView(View):

    def get(self, request):
        if(not request.user.is_authenticated):
            return HttpResponseRedirect(reverse("login"))

        profile = Profile.objects.get(user=request.user)
            
        return render(request, 'new_patient.html',
                      {"profile": profile})


    def post(self, request):

        if(not request.user.is_authenticated):
            return HttpResponseRedirect(reverse("login"))

        profile = Profile.objects.get(user=request.user)

        cpf = request.POST["user_cpf"].replace(".","").replace("-","")

        try:
            patient = Patient.objects.get(cpf=cpf)
            messages.error(request, "CPF já cadastrado.")
        except Exception as e:
            try:

                sex = Sex.objects.get(slug=request.POST["user_sex"])

                patient = Patient()
                patient.cpf = cpf
                patient.name = request.POST["user_name"]
                patient.email = request.POST["user_email"]
                patient.birthday = datetime.datetime.strptime(request.POST["user_birthday"],
                                                              "%d/%m/%Y").strftime("%Y-%m-%d")
                patient.weight = request.POST["user_weight"]
                patient.height = request.POST["user_height"]
                patient.sex = sex
                patient.save()

                messages.success(request, "Paciente cadastrado com sucesso!")
            
            except Sex.DoesNotExist as e:
                messages.error(request, "Sexo inválido!")
            
            except Exception as e:
                messages.error(request, str(e))

        return render(request, 'new_patient.html',
                      {"profile": profile})


class ListPatientView(View):

    def get(self, request):
        if(not request.user.is_authenticated):
            return HttpResponseRedirect(reverse("login"))

        profile = Profile.objects.get(user=request.user)

        patients = Patient.objects.all()
        paginator = Paginator(patients, 25)

        page = request.GET.get('page')
        patients = paginator.get_page(page)
            
        return render(request, 'list_patient.html',
                      {"patients": patients,
                       "profile": profile})


class NewExamView(View):

    def get(self, request):
        if(not request.user.is_authenticated):
            return HttpResponseRedirect(reverse("login"))

        profile = Profile.objects.get(user=request.user)

            
        return render(request, 'new_exam.html',
                      {"profile": profile})