from django import template

from main.models import Url
from main.permissions import url_permission_list

register = template.Library()


@register.simple_tag(name="get_urls", takes_context=True)
def urls(context):
    request = context['request']
    return url_permission_list(request.user)


