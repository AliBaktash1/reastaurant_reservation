from rest_framework import generics
from .models import Customer, Restaurant, Table, Reservation, Food, FoodReservation, Payment
from .serializers import (CustomerSerializer, RestaurantSerializer, TableSerializer,
                          ReservationSerializer, FoodSerializer, FoodReservationSerializer,
                          PaymentSerializer)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .models import Customer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedOrReadOnly  # Custom permission
from .models import Customer, Restaurant, Table, Reservation, Food, FoodReservation, Payment
from .serializers import (CustomerSerializer, RestaurantSerializer, TableSerializer,
                          ReservationSerializer, FoodSerializer, FoodReservationSerializer,
                          PaymentSerializer)

# Customer Views
class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict update/delete


# Restaurant Views
class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict update/delete


# Table Views
class TableListCreate(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict update/delete


# Reservation Views
class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict update/delete


# Food Views
class FoodListCreate(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict update/delete


# FoodReservation Views
class FoodReservationListCreate(generics.ListCreateAPIView):
    queryset = FoodReservation.objects.all()
    serializer_class = FoodReservationSerializer

class FoodReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodReservation.objects.all()
    serializer_class = FoodReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict update/delete


# Payment Views
class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict update/delete

# Registration View
class RegisterCustomer(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password or not name:
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        if Customer.objects.filter(email=email).exists():
            return Response({"error": "Email already in use."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user in the database
        customer = Customer.objects.create(name=name, phone=phone, email=email)
        user = User.objects.create_user(username=email, password=password, email=email)

        return Response({"message": "Customer registered successfully"}, status=status.HTTP_201_CREATED)


# Login View
class LoginCustomer(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)