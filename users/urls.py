from django.urls import path, include

from rest_framework import routers

from users.views import login_views, register_views, user_info_views, logout_views

router = routers.DefaultRouter()
router.register('login', login_views.Login, basename='login')
router.register('register', register_views.Register, basename='register')
router.register('logout', logout_views.Logout, basename='logout')
router.register('me', user_info_views.UserInfo, basename='me')

urlpatterns = [
    path('', include(router.urls))
]
