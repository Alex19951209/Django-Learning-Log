"""users URL Configuration"""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Додати уставні URL auth (автентифікації)
    path('', include('django.contrib.auth.urls')),
    # Сторінка реєстрації.
    path('register/', views.register, name='register'),
    # Сторінка для виходу із акаунта.
    path('logout_user', views.logout_user, name='logout'),
]