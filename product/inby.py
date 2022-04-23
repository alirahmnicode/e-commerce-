def increase_buyer(order):
    for product in order.products.all():
        product.sales_count += 1

    