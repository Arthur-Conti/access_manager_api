from rest_framework import permissions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from users.models import User

from core.auth.authentication import CustomUserAuthentication


class Logout(ViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'see you later'}

        return response
