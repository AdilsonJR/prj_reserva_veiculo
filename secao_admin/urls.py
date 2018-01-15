from django.urls import path
from . import views

app_name = 'administrador'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastro-funcionario/', views.cadastro_funcionario, name='cadastro_funcionario'),    
    path('cadastro-modelo/', views.cadastro_modelo, name='cadastro_modelo'),
    path('cadastro-veiculo/', views.cadastro_veiculo, name='cadastro_veiculo'),
    path('veiculos-disponiveis/', views.veiculos_disponiveis, name='veiculos_disponiveis'),                            
]
