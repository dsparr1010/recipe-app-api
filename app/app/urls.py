from django.contrib import admin
from django.urls import path, include
from user import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include(user_urls)),
]
