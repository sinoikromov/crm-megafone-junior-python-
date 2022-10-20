from django.urls import path
from .views import (ListProblem, CreateProblem, UpdateProblem,
                    CreateCategoryProblem, ActiveStatusProblem, DoneStatusProblem,
                    CanceledStatusProblem)

urlpatterns = [
    path('', ListProblem.as_view(), name='list_problem'),
    path('create/', CreateProblem.as_view(), name='create_problem'),
    path('<int:pk>/', UpdateProblem.as_view(), name='update_problem'),
    path('create_cat/', CreateCategoryProblem.as_view(), name='create_cat'),
    path('active_status/', ActiveStatusProblem.as_view(), name='active_status'),
    path('done_status/', DoneStatusProblem.as_view(), name='done_status'),
    path('canceled_status/', CanceledStatusProblem.as_view(), name='canceled_status'),


]
