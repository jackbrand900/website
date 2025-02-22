from django.urls import path
from . import views

urlpatterns = [
    path('add-example/', views.add_example_book, name='add_example_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]