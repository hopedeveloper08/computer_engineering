from django.urls import path
from .views import overview, currency_info, signal


urlpatterns = [
    path('overview/', overview, name='overview'),
    path('currency_info/<str:symbol>/', currency_info, name='currency_info'),
    path('signal/', signal, name='signal'),
]
