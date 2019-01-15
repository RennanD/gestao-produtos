from django.urls import path, include
from .views import novo_produto, lista_produto, update,delete



urlpatterns = [
    path('novo-produto/', novo_produto, name = "novo-produto"),
    path('', lista_produto, name = "lista-produto"),
    path('update/<int:id>', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
   
]
