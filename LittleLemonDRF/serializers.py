from rest_framework import serializers
from .models import MenuItem, Category
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User

# class RatingSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(
#         queryset = User.objects.all(),
#         default = serializers.CurrentUserDefault()
#     )
#     class Meta:
#         model = Rating
#         fields = ['user', 'menu_item_id', 'rating']
#         validators = [UniqueTogetherValidator(queryset=Rating.objects.all(),
#                                               fields = ['user', 'menuitem_id'])]
#         exta_kwargs = {
#             'rating': {'max_value': 5, "min_value": 0},
#             }

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']
        
class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','category','category_id']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    menuitem = MenuItemSerializer(read_only = True)
    class Meta:
        model= Cart
        fields = ['user', 'menuitem', 'quantity', 'unit_price', 'price', 'menuitem_id', 'menuitem', 'user_id', 'user']

class OrderSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
      )
    delivery_crew= serializers.PrimaryKeyRelatedField(
          queryset=User.objects.filter(groups__name='delivery_crew'),
          
          label='Delivery crew member'
      )
    class Meta:
        model = Order
        fields = ['user_id', 'user','delivery_crew', 'delivery_crew_id','status', 'total', 'date' ]

    