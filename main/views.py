from django.shortcuts import render, redirect
from .models import Carro

def criar_carro(request):
    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')


        carro = Carro(modelo=modelo, marca=marca, ano=ano, cor=cor)
        carro.save()

        return redirect('forms-carros')
    
    else:
        return render(request, 'main/index.html')

# Create your views here.