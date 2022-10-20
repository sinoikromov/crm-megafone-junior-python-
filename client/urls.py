from django.urls import path
from .views import (
    ListClientView, CreateClientView, DetailClientView,
    DeleteClientView, CreateClientProblemView, SearchResultsListView,
    )

urlpatterns = [
    path('', ListClientView.as_view(), name='list_client'),
    path('create/', CreateClientView.as_view(), name='create_client'),
    path('<int:pk>/', DetailClientView, name='detail_client'),
    path('delete/<int:pk>/', DeleteClientView.as_view(), name='delete_client'),
    path('create_client_problem/<int:pk>/', CreateClientProblemView.as_view(), name='create_client_problem'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
