from django.urls import path
from . import views

urlpatterns = [
    path('user_lessons/', views.user_lessons, name='user_lessons'),
    path('products/<int:product_id>/lessons/', views.product_lessons, name='product_lessons'),
    path('products/statistics/', views.product_statistics, name='product_statistics'),
]
