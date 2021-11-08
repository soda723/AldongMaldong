from django.urls import path 
from . import views

app_name = 'sub1app'
urlpatterns = [
    path('', views.searchRC, name='searchRC'),
]
