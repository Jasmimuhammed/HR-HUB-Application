from django.urls import path
from . import views

app_name = 'dashboard'   # Namespace for the dashboard app

urlpatterns = [
    path('dash_view', views.dashboard, name='dash_view'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('topbar', views.topbar, name='topbar'),
    path('footer', views.footer, name='footer'),
]
