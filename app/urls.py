from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('chatView/', views.chatView),
    path('token_balance/', views.token_balance),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
]