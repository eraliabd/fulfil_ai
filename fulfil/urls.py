from django.urls import path
from .views import home
app_name = 'fulfil'

urlpatterns = [
    path('', home, name='home'),
]
