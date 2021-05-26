"""Credicxo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from testapp.views import RegisterAPI,ChangePasswordView
from knox import views as knox_views
from testapp.views import LoginAPI

from testapp import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
router=routers.DefaultRouter()
# router.register('api',views.EmployeeCRUDCBV,base_name='api')
router.register('api',views.StudentCBV)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include(router.urls)),
     path('api/register/', RegisterAPI.as_view(), name='register'),
     path('api/login/', LoginAPI.as_view(), name='login'),
     # path('api/token',TokenObtainPairView.as_view()),
     #
     # path('api/token/refresh',TokenRefreshView.as_view()),
     url(r'^auth-jwt/', obtain_jwt_token),
     url(r'^auth-jwt-refresh/', refresh_jwt_token),
      url(r'^auth-jwt-verify/', verify_jwt_token),
     path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
     path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
     path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
     path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]
