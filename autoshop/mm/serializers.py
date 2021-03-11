from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'slug', 'price', 'description']


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name='product-detail',  # სახელის მიხედვით იღებს ურლ-ს
        queryset=Product.objects.all()
        # read_only=True -ზე ველს საერთოდ არ გამოიტანს ქვევით create-ში.
    )

    class Meta:
        model = Category
        fields = '__all__'

