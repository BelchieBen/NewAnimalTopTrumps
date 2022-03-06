from .auth_urls import auth_urlpatterns
from .urls import main_urlpatterns

urlpatterns = main_urlpatterns + auth_urlpatterns