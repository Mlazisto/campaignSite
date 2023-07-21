from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('', views.volunteers_view, name='volunteers'),
    path('signup/', views.signup_view, name='signup')
]