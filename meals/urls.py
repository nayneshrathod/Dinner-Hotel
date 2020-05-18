from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from meals import views

app_name = 'meals'
urlpatterns = [
    path('<slug:slug>/', views.details, name='meals_details'),
    path('', views.list, name='meal_list'),
    path('sms/', views.sample),
    path('list/', views.index),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
