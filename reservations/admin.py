from django.contrib import admin
from .models import Customer, Restaurant, Table, Reservation, Food, FoodReservation, Payment

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Food)
admin.site.register(FoodReservation)
admin.site.register(Payment)

