from django.contrib import admin
from django.urls import path
from baxify import views

urlpatterns = [
    path('', views.index, name="index"),
    path('service/', views.service, name="service"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('cal/', views.cal)
#   path('submitForm/', views.submitForm, name="submitForm")
]