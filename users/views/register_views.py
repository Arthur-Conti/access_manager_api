from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from users.serializers.users_serializers import UserSerializer


class Register(ViewSet):

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_serialized = UserSerializer(user).data

        return Response(user_serialized)
