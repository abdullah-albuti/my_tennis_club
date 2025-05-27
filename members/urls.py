from django.urls import path
from . import views

urlpatterns = [
        path('testing/', views.testing, name='testing'),  
        path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path("logout", views.logout_request, name="logout"),

]