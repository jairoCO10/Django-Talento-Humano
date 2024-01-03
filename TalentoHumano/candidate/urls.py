from django.urls import path
from . import views

urlpatterns = [
    path('candidatos/', views.candidato_list),
    path('candidatos/<str:iduuid>/', views.candidato_detail),
    path('candidatos/delete/<str:iduuid>/', views.candidato_delete),
    path('candidatos/update/<str:iduuid>/', views.candidato_update),
    # Otros paths si tienes más vistas
]
