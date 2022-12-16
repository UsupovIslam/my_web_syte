from django.urls import path
from .views import index, create

urlpatterns = [
    path('', index, name='name'),
    path('create/', create, name='create.html'),
]