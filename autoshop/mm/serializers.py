from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    cart = serializers.HyperlinkedRelatedField(
        view_name='cart-detail',
        queryset=Cart.objects.all()
    )

    class Meta:
        model = User
        fields = ['id', 'url', 'cart', 'username']


class ProductSerializer(serializers.ModelSerializer):
    cart_item = serializers.PrimaryKeyRelatedField(many=True, queryset=CartItem.objects.all())
    # slug = serializers.HyperlinkedIdentityField(view_name='product-slug', format='html')

    class Meta:
        model = Product
        fields = ['id', 'url', 'title', 'category', 'slug', 'cart_item', 'price', 'description']


class CategorySerializer(serializers.ModelSerializer):
    count_product = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ['id', 'url', 'title', 'order', 'count_product', 'product_cat']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'url', 'title', 'products']
        # fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.title')
    p_price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=CartItem.objects.all())

    class Meta:
        model = Cart
        fields = ['id', 'owner', 'items']
        # fields = '__all__'


