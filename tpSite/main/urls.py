from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('test1/', Test1.as_view(), name='test1'),
    path('test2/', Test2.as_view(), name='test2'),
]
