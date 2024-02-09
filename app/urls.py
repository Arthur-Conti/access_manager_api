from django.contrib import admin
from django.urls import path, include

from users import urls as user_urls
from access import urls as access_urls
from password_generator import urls as pass_gen_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(user_urls)),
    path('access/', include(access_urls)),
    path('passgen/', include(pass_gen_urls))
]