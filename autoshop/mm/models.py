from django.db import models
from django.db.models import CASCADE, PROTECT

"""
საიტი ავტომყვარულებისათვის: მანქანები, სერვისი, ნაწილები
"""


class Category(models.Model):
    title = models.CharField(max_length=24)
    order = models.CharField(max_length=24)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=24)
    products = models.ManyToManyField(to='Product', related_name='product_tag', related_query_name='product_tags')

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(to='Category', on_delete=CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class CartItem(models.Model):
    product = models.ForeignKey(to='Product', on_delete=CASCADE, related_name='cart_item')
    quantity = models.IntegerField()
    order = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    cart = models.ForeignKey(to='Cart', related_name='items', on_delete=PROTECT)


class Cart(models.Model):
    owner = models.OneToOneField(to='auth.User', on_delete=PROTECT)
