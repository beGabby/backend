from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('user.urls')),
]
#docker-compose run web python3 manage.py migrate
# tworzenie super user docker-compose run web python3 manage.py createsuperuser