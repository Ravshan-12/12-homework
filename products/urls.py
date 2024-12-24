from django.urls import path
from products import views


appname = "products"



urlpatterns = [
    path('list/', views.product_list, name='list'),
    path('about/', views.about, name='about'),
    path('create/' , views.product_create, name='create'),
    path('detail/<int:product_id>/', views.product_detail, name='detail'),
    path('delete/<int:product_id>/', views.product_delete, name='delete'),
]