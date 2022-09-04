from django.urls import path
from .views import mainlist

urlpatterns = [
    path('', mainlist , name="main"),
    
]