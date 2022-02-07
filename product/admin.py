from django.contrib import admin
from .models import Product , CategoryForOptions , Option , CategoryForProduct


admin.site.register(Product)
admin.site.register(CategoryForOptions)
admin.site.register(Option)
admin.site.register(CategoryForProduct)
