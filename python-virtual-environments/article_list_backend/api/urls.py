from django.urls import path
from .views import Index

#step-2a

urlpatterns = [
    path('', Index),
]