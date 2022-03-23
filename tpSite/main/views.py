from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, CreateView

from main.models import Url


class Main(ListView):
    model = Url
    template_name = 'main/main.html'


class Test1(DetailView):
    template_name = 'main/test1.html'


class Test2(DetailView):
    template_name = 'main/test2.html'


class UrlDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'main.view_url'
    model = Url
