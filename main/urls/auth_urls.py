from django.urls import path
from ..Views import auth_views

auth_urlpatterns = [
    path('register/',auth_views.register.as_view(), name='register'),
    path('login/',auth_views.Login.as_view(), name='login'),
]