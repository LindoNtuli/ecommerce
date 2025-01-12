#product serializers
from rest_framework import serializers
from .models import Product, Category, CustomUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image_url', 'created_date', 'stock', 'category_id']

    def validate(self, data):
        if data['price'] <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        if data['stock_quantity'] < 0:
            raise serializers.ValidationError("Stock Quantity cannot be negative.")
        if not data['name']:
            raise serializers.ValidationError("Product name is required.")
        return data

#Serializers for User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
