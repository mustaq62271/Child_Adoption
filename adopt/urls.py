from django.urls import path
from . import views
urlpatterns = [
    path('clientdetails/',views.clientdetails,name='clientdetails'),
    path('child-reg/',views.registration,name='child-reg'),
]
