from app.views import home, about, contact, recipe_detail_view
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('food', recipe_detail_view, name='food'),
]
