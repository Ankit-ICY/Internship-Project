from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.home ,name = "home"),
    path('contact/', views.contact ,name="contact"),
    path('users', views.users ,name="users"),



]
