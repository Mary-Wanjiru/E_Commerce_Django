from django.urls import path
from . import views

app_name = 'My_Ecommerce'
urlpatterns = [
    path('', views.product_list, name='product_list'), 
]