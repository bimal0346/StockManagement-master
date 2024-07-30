from rest_framework import serializers
from .models import Inventory,User_stock,All_Stock,Individual_Stock


class All_Stock_serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Stock
        fields = '__all__'

class User_Stock_serailizer(serializers.ModelSerializer):

    class Meta:
        model = User_stock
        fields = '__all__'

class Inventory_serializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'
class Individual_Stock_serializer(serializers.ModelSerializer):

    class Meta:
        model = Individual_Stock
        fields = '__all__'
