from django.shortcuts import render, redirect
from django.utils import timezone
from secao_admin.models import Funcionario, Veiculo, Reservas
from django.contrib import messages


def home(request):
    return render(request,'home-funcionario.html')

def formulario_reserva(request):
    if request.method == "POST":
        funcionario = request.POST['funcionario']
        veiculo = request.POST['veiculo']
        data_devolucao = request.POST['data_devolucao']

        f = Funcionario.objects.get(pk=funcionario)
        v = Veiculo.objects.get(pk=veiculo)
        vid = v.id_veiculo
        fid = f.id_funcionario
        r = Reservas(data_reserva = timezone.now(),
                    data_devolucao = data_devolucao,
                    fk_funcionario_id = fid, 
                    fk_veiculo_id = vid
                    )
        r.save()
        v.estado = 'reservado'
        v.save()

        messages.success(request, 'reserva do carro '+ v.nome +' para o funcionario '+f.nome+' feita com sucesso!!')
        
        return redirect('funcionario:formulario_reserva')    

    else:    
        veiculos = Veiculo.objects.all().filter(estado = 'disponivel')
        funcionarios = Funcionario.objects.all()
        return render(request, 'formulario-reserva.html',
        {'veiculos': veiculos, 'funcionarios' : funcionarios})


def veiculos_reservados_por_funcionarios(request):

    funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        
    
        funcionario = int(request.POST['funcionario'])
        f = Funcionario.objects.get(pk=funcionario)
        veiculos = f.veiculos.all()

        return render(request, 'veiculos-reservados-por-funcionarios.html',
        {'funcionarios' : funcionarios, 'f': f,'veiculos': veiculos})        
    else:
        
       
        return render(request, 'veiculos-reservados-por-funcionarios.html',
        {'funcionarios' : funcionarios})

def cancela_reserva(request, id_veiculo, id_funcionario):
    
    r = Reservas.objects.filter(fk_veiculo_id=id_veiculo, fk_funcionario_id=id_funcionario)
    r.delete()
    v = Veiculo.objects.get(pk=id_veiculo)
    v.estado = "disponivel"
    v.save()
    messages.success(request, 'reserva cancelada com sucesso!!')
        
    return redirect('funcionario:veiculos_reservados_por_funcionarios')


def formulario_editar(request, id_veiculo, id_funcionario):
    funcionario = Funcionario.objects.get(pk=id_funcionario)
    veiculo = Veiculo.objects.get(pk=id_veiculo)
    veiculos = Veiculo.objects.all().filter(estado = 'disponivel').exclude(pk=veiculo.id_veiculo)        
        
    return render(request, 'formulario-editar-reserva.html',
    {'funcionario' : funcionario,'veiculo' : veiculo, 'veiculos' : veiculos,
    'id_old_veiculo' : id_veiculo})


def editar_reserva(request):
    
    if request.method == "POST":
        
        id_old_veiculo = request.POST['old_veiculo']
        id_funcionario = request.POST['id_funcionario']
        id_novo_veiculo = request.POST['veiculo']

        r = Reservas.objects.get(fk_veiculo_id=id_old_veiculo, fk_funcionario_id=id_funcionario)
        r.fk_veiculo_id = id_novo_veiculo
        r.save()

        #muda o estado do antigo veiculo
        v = Veiculo.objects.get(pk=id_old_veiculo)
        v.estado = 'disponivel'
        v.save()

        #muda o estado do novo veiculo
        v = Veiculo.objects.get(pk=id_novo_veiculo)
        v.estado = 'reservado'
        v.save()

        messages.success(request, 'reserva editada com sucesso!!')
        return redirect('funcionario:veiculos_reservados_por_funcionarios')

