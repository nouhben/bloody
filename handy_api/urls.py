from django.urls import path, include
from .views import hello, home
urlpatterns = [
    path('', home, name='unicornHome'),
    #path('unicorn/', include('handy_api.urls')),
]
