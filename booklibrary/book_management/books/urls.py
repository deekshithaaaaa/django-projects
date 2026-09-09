from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('edit/<int:num>',views.edit),
    path('delete/<int:num>',views.delete)
]