
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from initiativeTrackerApi.views import login_user, register_user

urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
    path('register', login_user),
    path('login', authenticate),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

]
