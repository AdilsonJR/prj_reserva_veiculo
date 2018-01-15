from django.shortcuts import render, redirect
from .formularios.forms import Formulario_funcionario, Formulario_modelo
from .models import Funcionario, Modelo, Veiculo
from django.urls import reverse
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home-admin.html')

def cadastro_funcionario(request):
    if request.method == "POST":
        form = Formulario_funcionario(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            funcionario = Funcionario(nome=nome)
            funcionario.save()

        messages.success(request, 'funcionario %s cadastrado com sucesso cadastrado com sucesso!!' % nome)
        
        return redirect('administrador:cadastro_funcionario')
    else:
        form = Formulario_funcionario()
        return render(request,'formulario-funcionario.html', {'formulario_funcionario': form})    

def cadastro_modelo(request):
    if request.method == "POST":
        form = Formulario_modelo(request.POST)
        if form.is_valid():
            modelo = form.cleaned_data['modelo']
            modelo = Modelo(modelo=modelo)
            modelo.save()
            
            messages.success(request, 'Modelo %s cadastrado com sucesso!!' % modelo)

        return redirect('administrador:cadastro_modelo')            
    else:
        form_modelo = Formulario_modelo()
        return render(request,'formulario-modelo.html', {'formulario_modelo': form_modelo})

def cadastro_veiculo(request):
    if request.method == "POST":
        nome = request.POST['nome']
        placa = request.POST['placa']
        data_fabricacao = request.POST['data_fabricacao']
        modelo = int(request.POST['modelo'])
        estado = request.POST['estado']        
        nome_comcatenado = nome + '/' + placa

        m = Modelo.objects.get(pk=modelo)
      
        m.veiculo_set.create(
            placa = placa, 
            nome = nome_comcatenado,
            data_fabricacao = data_fabricacao,
            estado = estado,
            fk_modelo_id = modelo)
        m.save()

        messages.success(request, 'veiculo cadastrado com sucesso cadastrado com sucesso!!')
        
        return redirect(reverse('administrador:cadastro_veiculo'))    

    else:
        modelos = Modelo.objects.all()
        return render(request,'formulario-veiculo.html', {'modelos': modelos})    

def veiculos_disponiveis(request):
        veiculos = Veiculo.objects.all().filter(estado='disponivel')
        return render(request,'tb-veiculos-disponiveis.html', {'veiculos': veiculos})    