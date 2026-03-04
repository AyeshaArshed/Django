from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def datetime_data():
    return datetime.now()


@register.filter
def get_value(val):
    return val.upper()

