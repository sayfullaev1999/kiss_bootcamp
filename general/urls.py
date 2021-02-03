from django.urls import path
from .views import home
from .views import about
from .views import contact_us

urlpatterns = [
    path('', home, name='home_url'),
    path('about/', about, name='about_url'),
    path('contactus/', contact_us, name='contact_us_url')
]