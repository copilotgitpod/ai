from django.urls import path
from .views import RandomNewsView

urlpatterns = [
    path('random-news/', RandomNewsView.as_view(), name='random-news'),
]
