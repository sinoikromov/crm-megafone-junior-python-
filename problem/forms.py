from django import forms
from agents.models import Problem, Category


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = '__all__'


class CategoryProblemForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
