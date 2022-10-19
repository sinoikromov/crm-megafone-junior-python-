from django import forms
from .models import Agent


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'first_name',
            'last_name',
            'password',
            'email',
            'is_front_agent',
            'is_back_agent',
            'age',
            'phone_number',
            'gender',


        )


