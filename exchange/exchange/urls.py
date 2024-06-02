from django.contrib import admin
from django.urls import path, include
from account.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('account/', include('account.urls')),
    path('market/', include('market.urls')),
]
