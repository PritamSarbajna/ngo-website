from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.explore, name='explore'),
    path('contact/', views.contact, name='contact'),
    path('contact-saved/', views.contact_saved, name='contactSaved'),
]