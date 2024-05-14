from django.urls import path
from . import views

url_patterns = [
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>/', views.SingleItemView.as_view()),
    path('groups/manager/users/', views.ManagerUsersView.as_view()),
    path('groups/manager/users/<int:pk', views.ManagerSingleUserView.as_view()),
    path('groups/delivery-crew/users', views.Delivery_Crew_Management.as_view()),
    path('groups/delivery-crew/users/<int:pk>/', views.Delivery_Crew_Management_Single_View.as_view()),
    path('cart/menu-items/', views.Customer_Cart.as_view()),
    path('orders/', views.Orders_view.as_view()),
    path('orders/<int:pk>/', views.Single_Order_View.as_view()),

]