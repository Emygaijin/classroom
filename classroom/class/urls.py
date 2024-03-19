from django.urls import path
from .views import courses, display, home

urlpatterns = [
    path('', home, name='home'),
    path('course/', courses, name='courses'),
    path('display/<int:serial>/', display, name='display'),
]
