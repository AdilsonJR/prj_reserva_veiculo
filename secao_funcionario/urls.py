from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'funcionario'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('formulario-reserva/', views.formulario_reserva, name='formulario_reserva'),
    path('veiculos-reservados-por-funcionario/',
    views.veiculos_reservados_por_funcionarios, name='veiculos_reservados_por_funcionarios'),           
    url('^veiculos-reservados-por-funcionario/(?P<id_funcionario>.+)/(?P<id_veiculo>.+)/$', views.cancela_reserva, name='reserva_cancelada'),
    url('^formulario-editar-reserva/(?P<id_funcionario>.+)/(?P<id_veiculo>.+)/$', views.formulario_editar, name='formulario_editar'),    
    url('^editar-reserva/$', views.editar_reserva, name='editar_reserva'),        
]
