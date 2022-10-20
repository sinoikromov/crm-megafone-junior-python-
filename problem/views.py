from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from agents.models import Problem
from .forms import CategoryProblemForm, ProblemForm
from django.urls import reverse_lazy
from django.views import generic


class ListProblem(LoginRequiredMixin, generic.ListView):
    template_name = 'problem/list_problem.html'
    queryset = Problem.objects.all()

    def get_success_url(self):
        return reverse_lazy('list_problem')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = Problem.objects.filter(status='active').count()
        context['done'] = Problem.objects.filter(status='done').count()
        context['canceled'] = Problem.objects.filter(status='canceled').count()
        # context["comments"] = comments
        # context["total_comments"] = comments.count()
        return context


class CreateProblem(LoginRequiredMixin, generic.CreateView):
    template_name = 'problem/create_problem.html'
    form_class = ProblemForm

    def get_success_url(self):
        return reverse_lazy('list_problem')


class UpdateProblem(LoginRequiredMixin, generic.UpdateView):
    template_name = 'problem/update_problem.html'
    form_class = ProblemForm
    queryset = Problem.objects.all()
    context_object_name = 'problem'

    def get_success_url(self):
        return reverse_lazy('list_problem')


class CreateCategoryProblem(LoginRequiredMixin, generic.CreateView):
    template_name = 'problem/create_category.html'
    form_class = CategoryProblemForm

    def get_success_url(self):
        return reverse_lazy('list_problem')


class ActiveStatusProblem(LoginRequiredMixin, generic.ListView):
    template_name = 'problem/filter_problem.html'

    def get_queryset(self):
        active_problem = Problem.objects.filter(status='active')
        return active_problem


class DoneStatusProblem(LoginRequiredMixin, generic.ListView):
    template_name = 'problem/filter_problem.html'

    def get_queryset(self):
        done_problem = Problem.objects.filter(status='done')
        return done_problem


class CanceledStatusProblem(LoginRequiredMixin, generic.ListView):
    template_name = 'problem/filter_problem.html'

    def get_queryset(self):
        canceled_problem = Problem.objects.filter(status='canceled')
        return canceled_problem
