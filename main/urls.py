from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path('', views.homepage, name='home'),
    path('home', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('order/', views.orderpage, name='order'),
]


