# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('user-info/', views.user_info_view, name='user_info_view'),
    path('user-info-display/', views.user_info_display, name='user_info_display'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
]
