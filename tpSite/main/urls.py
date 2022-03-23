from django.urls import path, include
from .views import *

urlpatterns = [
    path('main/', urls, name='main'),
    path('test1/', test1, name='test1'),
    path('test2/', test2, name='test2'),
]
