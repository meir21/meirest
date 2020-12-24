from django.urls import path
from main import views



app_name = "main"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.aboutpage, name='aboutpage')
    
]