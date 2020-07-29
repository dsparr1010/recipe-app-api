from django.contrib import admin
from django.urls import path, include
from user import urls as user_urls
from recipe import urls as recipe_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include(user_urls)),
    path('api/recipe/', include(recipe_urls))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
