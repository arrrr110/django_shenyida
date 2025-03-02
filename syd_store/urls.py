from django.urls import path
from .views import IndexView ,HealthDataListView

urlpatterns = [
    path('syd/', IndexView.as_view(), name='index'),
    path('test/', HealthDataListView.as_view(), name='test')
]