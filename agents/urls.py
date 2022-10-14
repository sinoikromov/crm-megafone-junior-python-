from django.urls import path
from .views import (
    ListAgentView, CreateAgentView, DetailAgentView, UpdateAgentView, AgentDeleteView
)

urlpatterns = [
    path('', ListAgentView.as_view(), name='list_agent'),
    path('create/', CreateAgentView.as_view(), name='create_agent'),
    path('<int:pk>/', DetailAgentView.as_view(), name='detail_agent'),
    path('update/<int:pk>/', UpdateAgentView.as_view(), name='update_agent'),
    path('delete/<int:pk>/', AgentDeleteView.as_view(), name='delete_agent')

]
