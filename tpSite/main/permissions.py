from django.http import Http404
from django.shortcuts import redirect


class MembersPermissionMixin:
    def has_permissions(self):
        urls = self.model.objects.all()
        print(urls)
        for url in urls:
            if url.url == self.request.get_full_path():
                return self.request.user in url.members.all()

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
