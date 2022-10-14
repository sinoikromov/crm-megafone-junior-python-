from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Agent
from .forms import AgentForm


class ListAgentView(generic.ListView):
    queryset = Agent.objects.all()
    template_name = 'agents/agents_list.html'


class DetailAgentView(generic.DetailView):
    template_name = 'agents/detail_agent.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'


class UpdateAgentView(generic.UpdateView):
    template_name = 'agents/update_agent.html'
    form_class = AgentForm
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse('list_agent')


class CreateAgentView(generic.CreateView):
    template_name = 'agents/create_agent.html'
    form_class = AgentForm

    def get_success_url(self):
        return reverse('list_agent')


class AgentDeleteView(generic.DeleteView):
    template_name = 'agents/delete_agent.html'
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse('list_agent')
