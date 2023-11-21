from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user_carpeta.models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from .forms import BeneficiaryForm
from  django.contrib import messages


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
                user = CustomUser.objects.create_user(username=request.POST['username'],
                                                      password=request.POST['password1'])
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


def ingresar(request):
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


def salir(request):
    logout(request)
    return redirect('home')


def panel_padrino(request):
    return render(request, 'panel_padrino.html')


def employee_panel(request):

    if request.method == 'POST':
        form = BeneficiaryForm(request.POST)
        if form.is_valid():
            employee_id = form.save(commit=False)
            employee_id.responsible = request.user
            employee_id.save()
            messages.success(request, 'Registro exitoso')
            return redirect('/employee_panel/')

    else:
        form = BeneficiaryForm()

    return render(request, 'employee_panel.html', {
        'form': form})

    return render(request, 'employee_panel.html')




