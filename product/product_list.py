from .models import Product


class ProductList:
    def __init__(self , query , category , sort , order):
        if query == 'recommend':
            self.title = 'recommends'
            self.products = Product.objects.filter(recommend=True)
        elif query == 'category':
            self.title = category
            self.products = Product.objects.filter(category__name=category)
        elif query == 'bestsellers':
            self.title = 'bestsellers products'
            self.products = Product.objects.all().order_by("-sales_count")

        self.sort = sort
        self.order = order

    def get_product(self , range=None):
        if self.sort and self.order:
                self.sort_obj()
        else:
            pass
        if range:
            next_products = int(range)
            next_products += 50
            previous_articles = next_products - 20
            obj = self.products[previous_articles:next_products]
            return self.data(obj)
        else:
            return self.products[:50]

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


    def sort_obj(self):
        if self.order == 'asc':
            order = str(self.sort)
        elif self.order == 'desc':
            order = f'-{self.sort}'
        return self.products.order_by(order)

