from django.urls import path
from general.views import home, about

urlpatterns = [
    path('', home, name='home_url'),
    path('about/', about, name='about_url')
]