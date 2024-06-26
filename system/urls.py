from django.urls import path
from .views import *

urlpatterns = [
    path('slide_list', slide_list, name='slide_list')
]