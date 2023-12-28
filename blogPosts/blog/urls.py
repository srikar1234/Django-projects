from django.urls import path
from . import views

#map urls of certain locations to be accessed in a certain way
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]
