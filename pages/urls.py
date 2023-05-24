from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('hello/',HomePageView,name = 'home')
]