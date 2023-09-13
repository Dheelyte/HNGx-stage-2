from django.urls import path
from .views import API, APIDetails

urlpatterns = [
    path('api/', API.as_view()),
    path('api/<str:id>/', APIDetails.as_view())
]
