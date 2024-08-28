from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_list, name='travel_list'),
    path('create/', views.create_travel_entry, name='create_travel_entry'),
    path('travel/<int:travel_id>/', views.travel_detail, name='travel_detail'),
]
