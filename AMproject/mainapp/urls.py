from django.urls import path 
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.main, name='main'), #main
    path('go_search/', views.go_search, name="go_search"),
    path('search_result/', views.search_result, name='search_result'),
]
