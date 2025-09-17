from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('add/', views.add_address, name='add_address'),
    path('edit/<int:pk>/', views.edit_address, name='edit_address'),
    path('delete/<int:pk>/', views.delete_address, name='delete_address'),
]
