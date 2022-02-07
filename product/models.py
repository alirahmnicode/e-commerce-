from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="product")
    options = models.ForeignKey("Option", on_delete=models.CASCADE ,blank=True, null=True)
    available = models.BooleanField(default=True)
    slug = models.SlugField(null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Option(models.Model):
    opt = models.CharField(max_length=200)
    category = models.ForeignKey("CategoryForOptions", on_delete=models.CASCADE)


class CategoryForOptions(models.Model):
    name = models.CharField(max_length=200)
