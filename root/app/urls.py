from app.views import home, about, contact, search,base, Fitnes
from django.urls import path

urlpatterns = [
    path('login', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('food', search, name='food'),
    path('', base, name='base'),
    path('Fitnes', Fitnes, name='Fitnes'),
    # path('profile', profile, name='profile'),
]
