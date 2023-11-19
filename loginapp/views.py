from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user_carpeta.models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt

import user_carpeta as UserPorpio


def Home(request):
    return render(request, 'home.html')

@csrf_exempt
def registro(request):

    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:

        if request.POST['password1'] == request.POST['password2']:

            try:
                user = CustomUser.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/panel_padrino/')
            except IntegrityError as e:
                print(e)
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': "Usuario ya existe"
                })

        return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': "Las contraseñas no coinciden"
        })


def ingresar (request):
    if request.method == 'GET':
        return render(request, 'ingresar.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'ingresar.html', {
                'form': AuthenticationForm,
                'error': 'Usuario invalido'
            })
        else:
            login(request, user)
            return redirect('/panel_padrino/')


def salir (request):
    logout(request)
    return redirect('home')

def panel_padrino (request):
    return render(request, 'panel_padrino.html')

def panel_apadrinado (request):
    return render(request, 'panel_apadrinado.html')




