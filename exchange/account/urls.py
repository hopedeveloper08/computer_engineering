from django.urls import path
from .views import register, login, authentication, logout


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('authentication/', authentication, name='authentication'),
    path('logout/', logout, name='logout'),
]
