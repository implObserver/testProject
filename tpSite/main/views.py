from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Url
from main.permissions import MembersPermissionMixin


class Main(LoginRequiredMixin, ListView):
    model = Url
    template_name = 'main/main.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class Test1(MembersPermissionMixin, ListView):
    model = Url
    template_name = 'main/test1.html'


class Test2(MembersPermissionMixin, ListView):
    model = Url
    template_name = 'main/test2.html'
