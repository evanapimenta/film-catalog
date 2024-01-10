from django import template
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def current_view_name(context):
    request = context['request']
    return resolve(request.path_info).url_name