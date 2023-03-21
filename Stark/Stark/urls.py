from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/login/",jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path("api/login-otp/",include('buyersApp.api.urls')),
]
