from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.models import Client, Problem
from django.db.models import Q
from .forms import ClientForm, ClientProblem


class ListClientView(LoginRequiredMixin, generic.ListView):
    queryset = Client.objects.all()
    template_name = 'client/list_client.html'


class CreateClientView(LoginRequiredMixin, generic.CreateView):
    template_name = 'client/create_client.html'
    form_class = ClientForm

    def get_success_url(self):
        return reverse('list_client')


# class DetailClientView2(LoginRequiredMixin, generic.DetailView):
#     template_name = 'client/detail_client.html'
#     context_object_name = "list_problem"


def DetailClientView(request, pk):
    client = Client.objects.get(pk=pk)
    queryset = Problem.objects.filter(client=client)
    context = {
        'client': client,
        'list_problem': queryset
    }
    return render(request, 'client/detail_client.html', context=context)


class DeleteClientView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'client/delete_client.html'
    queryset = Client.objects.all()

    def get_success_url(self):
        return reverse('list_client')


class CreateClientProblemView(LoginRequiredMixin, generic.CreateView):
    template_name = 'client/create_problem.html'
    form_class = ClientProblem

    def get_success_url(self):
        return reverse('list_client')

    def form_valid(self, form):
        problem = form.save(commit=False)
        problem.client = Client.objects.get(pk=int(str(self.request.path)[-2]))
        problem.save()
        return super(CreateClientProblemView, self).form_valid(form)


class SearchResultsListView(LoginRequiredMixin, generic.ListView):
    template_name = 'client/search_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        client_list = Client.objects.filter(Q(phone_number__icontains=query)
                                            | Q(patronymic__icontains=query)
                                            | Q(email__icontains=query))
        return client_list

