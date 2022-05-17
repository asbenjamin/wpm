from django.urls import path
from . import views

app_name = 'wpmin'

urlpatterns = [
    path('', views.index, name='index'),
    path('wpm/', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('add_url/', views.add_url, name='add_url'),
    path('get_contacts/', views.get_contacts, name='get_contacts'),
]