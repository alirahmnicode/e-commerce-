from atexit import register
from django import template

register = template.Library()

def counter(value):
    count = 0
    for i in value.values():
        count += i['quantity']
    return count


def price(p):
    price = str(p)
    new_price = ''
    n = 0
    for i in reversed(price):
        n+=1
        if n % 3 == 0 and n < len(price):
            new_price += f"{i} "
        else:
            new_price += i
    return f"${new_price[::-1]}"


register.filter('counter', counter)
register.filter('price', price)