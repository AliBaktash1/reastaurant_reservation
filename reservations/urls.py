from django.urls import path
from .views import (CustomerListCreate, CustomerDetail, RestaurantListCreate, RestaurantDetail,
                    TableListCreate, TableDetail, ReservationListCreate, ReservationDetail,
                    FoodListCreate, FoodDetail, FoodReservationListCreate, FoodReservationDetail,
                    PaymentListCreate, PaymentDetail)
from .views import RegisterCustomer, LoginCustomer
urlpatterns = [
    path('register/', RegisterCustomer.as_view(), name='register'),
    path('login/', LoginCustomer.as_view(), name='login'),
    # Customer URLs
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),

    # Restaurant URLs
    path('restaurants/', RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),

    # Table URLs
    path('tables/', TableListCreate.as_view(), name='table-list-create'),
    path('tables/<int:pk>/', TableDetail.as_view(), name='table-detail'),

    # Reservation URLs
    path('reservations/', ReservationListCreate.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),

    # Food URLs
    path('foods/', FoodListCreate.as_view(), name='food-list-create'),
    path('foods/<int:pk>/', FoodDetail.as_view(), name='food-detail'),

    # FoodReservation URLs
    path('food-reservations/', FoodReservationListCreate.as_view(), name='food-reservation-list-create'),
    path('food-reservations/<int:pk>/', FoodReservationDetail.as_view(), name='food-reservation-detail'),

    # Payment URLs
    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetail.as_view(), name='payment-detail'),
]
