from django.urls import path
from . import views
from cart import views as cart_views

app_name = 'chatbot'

urlpatterns = [
    path('chat/', views.chatbot_view, name='chatbot_chat'),
    path('add-to-cart/', cart_views.add_to_cart_api, name='add_to_cart_api'),
]
