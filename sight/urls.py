from django.urls import *
from .views import *

urlpatterns = [
    path('sight_list', sight_list, name='sight_list')
]