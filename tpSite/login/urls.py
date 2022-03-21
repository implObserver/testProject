from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('', user_login, name='home'),
]
