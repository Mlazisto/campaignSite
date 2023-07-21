from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register/', views.register_user, name='register'),
]