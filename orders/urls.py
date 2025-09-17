from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('api/', views.order_list_api, name='order_list_api'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('api/<int:pk>/', views.order_detail_api, name='order_detail_api'),
    path('create/', views.create_order, name='create_order'),
    path('<int:pk>/cancel/', views.cancel_order, name='cancel_order'),
    path('<int:pk>/pay/', views.payment, name='payment'),
    path('<int:pk>/track/', views.track_order, name='track_order'),
    path("success/<int:order_id>/", views.order_success, name="order_success"), 
]
