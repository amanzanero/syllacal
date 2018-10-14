from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('button/', views.index_example, name='upload')
]