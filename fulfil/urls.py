from django.urls import path
from .views import home, success
app_name = 'fulfil'

urlpatterns = [
    path('', home, name='home'),
    path('success/', success, name='success'),
]
