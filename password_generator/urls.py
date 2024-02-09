from django.urls import path, include

from rest_framework import routers

from password_generator.views.password_generator_views import PasswordGenerator


router = routers.DefaultRouter()
router.register('', PasswordGenerator, basename='pass_gen')


urlpatterns = [
    path('', include(router.urls))
]
