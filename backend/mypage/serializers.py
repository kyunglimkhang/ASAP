from rest_framework import serializers
from recommend.models import Item
from accounts.models import User
from .models import OrderDetail


class UserSerializer(serializers.ModelSerializer):
    order_history = serializers.StringRelatedField(many=True)
    keywords = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'address', 'keywords',
                  'like_items', 'cart_items', 'order_history']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['asin', 'title', 'price']
        extra_kwargs = {
            'asin': {'validators': []},
        }


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class NewOrderSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=serializers.CharField(max_length=50)
    )
    price = serializers.FloatField()