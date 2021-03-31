from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('auth/', obtain_auth_token)
]
#docker-compose run web python3 manage.py migrate
# tworzenie super user docker-compose run web python3 manage.py createsuperuser