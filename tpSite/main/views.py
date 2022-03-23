from django.shortcuts import get_object_or_404, render

from main.models import Url


def view_urls(request, url_id):
    url_item = get_object_or_404(Url, pk=url_id)
    return render(request, 'main/main.html', {"url_item": url_item})


def urls(request):
    pass


def test1(request):
    pass


def test2(request):
    pass
