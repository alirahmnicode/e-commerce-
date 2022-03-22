from multiprocessing.dummy import Value
from .models import Product, CategoryForProduct
from .data import data


def search_obj(query):
    if query != '':
        products = Product.objects.filter(name__icontains=query)
        category = CategoryForProduct.objects.filter(name__icontains=query)
        context = {"product": products, "category": category}
        search_result = {}
        for key , value in context.items():
            obj = data(value,key)
            search_result[key] = obj
        return search_result
    else:
        return 'nothing find...'