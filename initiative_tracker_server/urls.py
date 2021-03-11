
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import router
from initiativeTrackerApi.views import login_user, register_user

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

]
