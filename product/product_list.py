from .models import Product


class ProductList:
    def __init__(self ,category , sort , order):
        self.products = Product.objects.filter(category__name=category)
        self.sort = sort
        self.order = order

    def get_product(self , range=None):
        # with ajax request
        sort_by = self.sort_obj()
        if range and sort_by:
            next_products = int(range)
            next_products += 5
            previous_articles = next_products - 5
            if sort_by:
                obj = self.products.order_by(sort_by)[previous_articles:next_products]
            else:
                obj = self.products[previous_articles:next_products]
            return self.data(obj)
        # first objects with get request
        elif sort_by:
            return self.products.order_by(sort_by)[:5]
        else:
            return self.products[:5]

    def sort_obj(self):
        # if filter request
        if self.order and self.sort:
            if self.order == 'asc':
                sort_by = str(self.sort)
            elif self.order == 'desc':
                sort_by = f'-{self.sort}'
            return sort_by

    def data(self , obj):
        # create list for jsonresponse
        data = []
        for product in obj:
            item = {
                "pk": product.pk,
                "name": product.name,
                "description": product.description,
                # "image": product.image.url,
                "slug": product.slug,
            }
            data.append(item)
        return data