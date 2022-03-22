def data(obj, type):
    data = []
    for product in obj:
        item = {
            "pk": product.pk,
            "name": product.name,
            
        }
        if type == "product":
            item["description"] = product.description
            item["price"] = product.price
            item["slug"] = product.slug
        try:
            item["image"] = product.image.url,
        except:
            pass
        data.append(item)
    return data
