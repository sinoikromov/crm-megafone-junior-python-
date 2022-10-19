from django.forms import ModelForm
from agents.models import Client, Problem


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ClientProblem(ModelForm):
    class Meta:
        model = Problem
        exclude = ['client']
