from .models import Product


class ProductList:
    def __init__(self ,category=None , sort=None , order=None , filter=None):
        self.products = Product.objects.filter(category__name=category)
        self.sort = sort
        self.order = order
        self.filter = filter

    def get_product(self , range=None):
        # with ajax request
        sort_by = self.sort_obj()
        if range:
            next_products = int(range)
            next_products += 5
            previous_articles = next_products - 5
            if sort_by:
                obj = self.products.order_by(sort_by)[previous_articles:next_products]
            elif self.filter:
                obj = self.filter_obj(self.products)[previous_articles:next_products]
            else:
                obj = self.products[previous_articles:next_products]
            return self.data(obj)
        # first objects with get request
        elif sort_by:
            return self.products.order_by(sort_by)[:5]
        elif self.filter:
            return self.filter_obj(self.products)
        else:
            return self.products[:5]

    def sort_obj(self):
        # if filter request
        if self.order or self.sort:
            if self.order == 'asc':
                sort_by = str(self.sort)
            elif self.order == 'desc':
                sort_by = f'-{self.sort}'
            return sort_by

    def filter_obj(self , products):
        filter_s = self.filter
        return products.filter(recommend=True)

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