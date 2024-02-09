from django.urls import path, include

from rest_framework import routers

from access.views import access_views

router = routers.DefaultRouter()
router.register('', access_views.AccessInfo, basename='access')

urlpatterns = [
    path('', include(router.urls)),
]
