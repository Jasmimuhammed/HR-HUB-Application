from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    
]
