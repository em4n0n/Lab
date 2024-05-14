from django.urls import path
from . import views

url_patterns = [
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>/', views.SingleItemView.as_view()),
    path('groups/manager/users/', views.ManagerUsersView.as_view()),
    path('groups/manager/users/<int:pk', views.ManagerSingleUserView.as_view()),


]