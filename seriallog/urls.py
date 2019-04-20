from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='seriallog-home'),
    path('seriallog_error/', views.seriallog_error, name='seriallog-error'),
]

