from rest_framework import permissions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from users.serializers.users_serializers import UserSerializer

from core.auth.authentication import CustomUserAuthentication


class UserInfo(ViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def list(self, request):
        user = request.user

        serializer = self.serializer_class(user).data

        return Response(serializer)
