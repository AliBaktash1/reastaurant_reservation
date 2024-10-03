from rest_framework import serializers
from .models import Customer, Restaurant, Table, Reservation, Food, FoodReservation, Payment


# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# Restaurant Serializer
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


# Table Serializer
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


# Reservation Serializer
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


# Food Serializer
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


# FoodReservation Serializer
class FoodReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodReservation
        fields = '__all__'


# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
