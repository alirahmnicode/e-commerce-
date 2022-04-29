from atexit import register
from django import template

register = template.Library()


def counter(value):
    count = 0
    for i in value.values():
        count += i["quantity"]
    return count


def price(p):
    price = str(p)
    new_price = ""
    n = 0
    for i in reversed(price):
        n += 1
        if n % 3 == 0 and n < len(price):
            new_price += f"{i}'"
        else:
            new_price += i
    return f"${new_price[::-1]}"


def get_url(url , page_number):
    url_pieces = url.split('page')
    url_pieces2 = url.split('&')
    new_url = ''
    if '?' in url:
        if len(url_pieces2) > 1 and url_pieces[0][-1] != '&': 
            page_number1 = f'&page={page_number}'
        else:
            page_number1 = f'page={page_number}'
        new_url = f'{url_pieces[0]}{page_number1}'
    else:
        new_url = f'{url_pieces[0]}?page={page_number}'
    return new_url


register.filter("counter", counter)
register.filter("price", price)
register.filter("get_url", get_url)
