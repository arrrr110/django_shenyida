from django.urls import path
from .views import IndexView

urlpatterns = [
    path('syd/', IndexView.as_view(), name='index'),
]