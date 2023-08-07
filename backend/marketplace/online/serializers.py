from rest_framework import serializers
from .models import * 



class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password","email","phoneno","address"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
class ProductModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductModelSerializers()

    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    # dish=DishModelSer(many=False,read_only=True) 
    class Meta:
        model=Reviews  
        fields=[
            'review',
            'rating',
            'date'
        ]     

    def create(self, validated_data):
        user= self.context.get("user")  
        product=self.context.get("product")
        return Reviews.objects.create(user=user,product=product,**validated_data)   



