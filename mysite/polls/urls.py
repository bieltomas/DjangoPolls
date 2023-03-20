from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pregunta_id>/', views.detalles, name='detalles'),
    path('<int:pregunta_id>/resultados/', views.resultados, name='resultados'),
    path('<int:pregunta_id>/votar/', views.votar, name='votar'),
]