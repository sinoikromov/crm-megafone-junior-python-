from django.shortcuts import render
from agents.models import Problem
from .forms import CategoryProblemForm, ProblemForm
from django.urls import reverse_lazy
from django.views import generic


class ListProblem(generic.ListView):
    template_name = 'problem/list_problem.html'
    queryset = Problem.objects.all()

    def get_success_url(self):
        return reverse_lazy('list_problem')


class CreateProblem(generic.CreateView):
    template_name = 'problem/create_problem.html'
    form_class = ProblemForm

    def get_success_url(self):
        return reverse_lazy('list_problem')


class UpdateProblem(generic.UpdateView):
    template_name = 'problem/update_problem.html'
    form_class = ProblemForm
    queryset = Problem.objects.all()
    context_object_name = 'problem'

    def get_success_url(self):
        return reverse_lazy('list_problem')


class CreateCategoryProblem(generic.CreateView):
    template_name = 'problem/create_category.html'
    form_class = CategoryProblemForm

    def get_success_url(self):
        return reverse_lazy('list_problem')


