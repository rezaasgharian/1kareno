from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile-Update/', profileUpdate, name='profile-update'),
]