from django.urls import path, include
from ..Views.views import *
from django.conf import settings
from django.conf.urls.static import static

main_urlpatterns = [
    path('',test.as_view(), name='home'),
    path('create/', create_room.as_view(), name='create_room'),
    path('join/<str:code>', join_room.as_view(), name='join_room')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
