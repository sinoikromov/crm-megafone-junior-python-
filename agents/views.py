from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Agent
from .forms import AgentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class ListAgentView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agents_list.html'

    def get_queryset(self):
        queryset = None
        if self.request.user.is_superuser:
            queryset = Agent.objects.all()
        return queryset


class DetailAgentView(LoginRequiredMixin, generic.DetailView):
    template_name = 'agents/detail_agent.html'
    context_object_name = 'agents'

    def get_queryset(self):
        queryset = None
        if self.request.user.is_superuser:
            queryset = Agent.objects.all()
        return queryset


class UpdateAgentView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/update_agent.html'
    form_class = AgentForm
    context_object_name = 'agents'

    def get_queryset(self):
        queryset = None
        if self.request.user.is_superuser:
            queryset = Agent.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('list_agent')


class CreateAgentView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create_agent.html'
    form_class = AgentForm

    def get_queryset(self):
        queryset = None
        if self.request.user.is_superuser:
            queryset = Agent.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('list_agent')


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/delete_agent.html'

    def get_queryset(self):
        queryset = None
        if self.request.user.is_superuser:
            queryset = Agent.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('list_agent')


class SearchResultsListView(generic.ListView):
    template_name = 'agents/search_agent.html'

    def get_queryset(self):
        client_list = None
        if self.request.user.is_superuser:
            query = self.request.GET.get('q')
            client_list = Agent.objects.filter(Q(phone_number__icontains=query)
                                               | Q(last_name__icontains=query)
                                               | Q(email__icontains=query))
        return client_list
