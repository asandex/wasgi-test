from django.urls import path

from . import views


urlpatterns = [
    path('sync-hi/', views.sync_hello_world),
    path('sync-hi-slow/', views.sync_hello_world_slow),
    path('async-hi-slow/', views.async_hello_world_slow),
]
