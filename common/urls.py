from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='common-home'),
    path('login/',auth_views.LoginView.as_view(template_name='common/login.html'), name='common-login'),
    path('register/',views.register, name='common-register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='common/logout.html'),name="common-logout")
]