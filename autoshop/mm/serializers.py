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
        fields = ['id', 'cart', 'username']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'slug', 'price', 'description']


class CategorySerializer(serializers.ModelSerializer):
    # product = serializers.CharField()
    # product = serializers.HyperlinkedRelatedField(
    #     view_name='product-detail',
    #     queryset=Product.objects.all()
    #     # read_only=True -ზე ველს საერთოდ არ გამოიტანს ქვევით create-ში.
    # )

    class Meta:
        model = Category
        fields = ['id', 'title', 'order', 'product_cat']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.CharField()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        # fields = ['id', 'owner']
        fields = '__all__'


