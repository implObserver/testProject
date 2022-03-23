from django.shortcuts import redirect

from main.models import Url
from users.models import CustomUser


def url_permission_list(user):
    paths = list()
    urls = Url.objects.all()
    for url in urls:
        if user in url.members.all():
            paths.append(url.url)
    return paths


class MembersPermissionMixin:

    def has_permissions(self):
        urls = Url.objects.all()
        for url in urls:
            if url.url == self.request.build_absolute_uri():
                return self.request.user in url.members.all()

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return redirect('main')
        return super().dispatch(request, *args, **kwargs)
