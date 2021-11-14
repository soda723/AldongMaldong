from django.urls import path 
from . import views

app_name = 'sub1app'
urlpatterns = [
    path('', views.searchRC, name='searchRC'),
    path('center_info/<int:obj_pk>', views.center_info, name='center_info'),
]
