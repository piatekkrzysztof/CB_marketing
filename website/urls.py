from django.urls import path
from . import views

urlpatterns = [
path('',views.home),
path('layout/',views.main),
path('o_nas/',views.about),
]