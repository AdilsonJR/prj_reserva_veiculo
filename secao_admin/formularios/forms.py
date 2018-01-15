from django import forms

class Formulario_funcionario(forms.Form):
    nome = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class': 'form-control mb-5'}),
            label = 'Nome do funcionario')

class Formulario_modelo(forms.Form):
    modelo = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class': 'form-control mb-5'}),
            label = 'Informe o nome do modelo')

