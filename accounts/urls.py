from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),       # root '/' shows login page
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),    # temporary placeholder home
]