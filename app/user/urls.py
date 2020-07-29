from django.urls import path

from . import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name = 'create'),
    path('token/', views.CreateTokenView.as_view(), name = 'token'),
    path('me/', views.ManageUserView.as_view(), name = 'me'),
]

# 85900c1b9401ef534a3de3069bf46a342a20fe6f
# ce53a1e498dae0aae08fb5b69ab8c20792376ef6