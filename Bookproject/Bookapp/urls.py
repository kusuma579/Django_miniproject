from django.urls import path
from .views import home, contact, profile,grade,users

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='profile'),
    path('grade/<int:marks>/', grade, name='grade'),
    path('/user',users,name='user'),
]