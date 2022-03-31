from atexit import register
from django import template

register = template.Library()

def counter(value):
    count = 0
    for i in value.values():
        count += i['quantity']
    return count


register.filter('counter', counter)