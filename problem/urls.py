from django.urls import path
from .views import ListProblem, CreateProblem, UpdateProblem, CreateCategoryProblem

urlpatterns = [
    path('', ListProblem.as_view(), name='list_problem'),
    path('create/', CreateProblem.as_view(), name='create_problem'),
    path('<int:pk>/', UpdateProblem.as_view(), name='update_problem'),
    path('create_cat/', CreateCategoryProblem.as_view(), name='create_cat')

]
