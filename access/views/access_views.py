from rest_framework import viewsets, permissions, exceptions
from rest_framework.response import Response

from access.models import Access
from users.models import User

from access.serializers import AccessSerializer

from core.authentication import CustomUserAuthentication

import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s:      %(message)s')
logging.basicConfig(level=logging.ERROR, format='%(levelname)s:         %(message)s')
                    

class AccessInfo(viewsets.ViewSet):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    lookup_value_regex = '[0-9]'
    serializer_class = AccessSerializer

    def list(self, request):
        user_email = request.user.email

        access = Access.objects.filter(user_id__email=user_email)
        access_serialized = self.serializer_class(access, many=True, context={'request': request}).data

        return Response(access_serialized)
    
    def retrieve(self, request, id):
        access = Access.objects.get(id=id)
        if str(request.user.email) == str(access.user_id):
            access_serialized = self.serializer_class(access, context={'request': request}).data
            return Response(access_serialized)
        else:
            raise exceptions.NotAuthenticated('You do not have access to this resource')
        
    def create(self, request):
        user = User.objects.get(email=request.user.email)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            access = serializer.create(user, serializer.validated_data)
            access_serialized = self.serializer_class(access).data
        else:
            logger.error(f'Serializer error: {serializer.errors}')
            raise ValueError(serializer.errors)
        
        return Response(access_serialized)
