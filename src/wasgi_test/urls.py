from django.urls import path

from . import views

urlpatterns = [
    path('sync-hi/', views.sync_hello_world),
    path('async-hi/', views.async_hello_world),
]
