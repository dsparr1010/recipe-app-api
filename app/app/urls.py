from django.contrib import admin
from django.urls import path, include
from user import urls as user_urls
from recipe import urls as recipe_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include(user_urls)),
    path('api/recipe/', include(recipe_urls))
]
