from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="product")
    options = models.ManyToManyField("Option", related_name="options", blank=True)
    category = models.ManyToManyField("CategoryForProduct", related_name="categores", blank=True)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=20, decimal_places=0 ,null=True)
    slug = models.SlugField(null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Option(models.Model):
    opt = models.CharField(max_length=200)
    category = models.ForeignKey(
        "CategoryForOptions", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.opt


class CategoryForOptions(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CategoryForProduct(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name