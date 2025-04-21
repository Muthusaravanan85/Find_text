
from django.urls import path
from text import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
]
