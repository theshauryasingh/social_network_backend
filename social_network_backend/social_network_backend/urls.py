"""
URL configuration for social_network_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from social_network_api import views
from rest_framework.routers import DefaultRouter
# from api.auth import CustomAuthToken

router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet, basename='users')
router.register(r'friendrequests', views.FriendRequestViewSet, basename='friendrequests')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken', CustomAuthToken.as_view())
    # path('signup', views.user_create),

]
