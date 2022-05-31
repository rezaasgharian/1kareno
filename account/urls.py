from django.urls import path
from .views import register, login, logout, profile, profileUpdate, changePassword

app_name = 'account'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile-update/', profileUpdate, name='profile-update'),
    path('change-password/', changePassword, name='change-password'),
]