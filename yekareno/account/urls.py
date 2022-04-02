from django.urls import path
from .views import register, login, forgetPassword

app_name = 'account'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('forget-password/', forgetPassword, name='forget_password'),
]