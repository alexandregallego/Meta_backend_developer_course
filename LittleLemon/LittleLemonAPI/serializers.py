from rest_framework import serializers
from .models import MenuItem, Category, Order
from django.contrib.auth.models import Group, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price',
                  'featured', 'category', 'category_id']


class OrderSerializer(serializers.ModelSerializer):

    delivery_crew_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew',
                  'status', 'total', 'date', 'delivery_crew_id']
        read_only_fields = ['id', 'user', 'delivery_crew', 'total', 'date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'id']
