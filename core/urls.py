from django.urls import path, include
from . import views


urlpatterns = [
    path('filter/',views.filter,name='filter'),
]