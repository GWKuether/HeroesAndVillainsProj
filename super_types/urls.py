from django.urls import path

from super_types import views

urlpatterns = [
    path('', views.super_types_list)
]
