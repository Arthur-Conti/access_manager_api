from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from password_generator.serializers.password_generator_serializers import PasswordGeneratorSerializer, PostPasswordGeneratorSerializer


class PasswordGenerator(ViewSet):

    serializer_class = PostPasswordGeneratorSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            password = serializer.create(serializer.validated_data)
            password_serialized = PasswordGeneratorSerializer.serialize(password).data
        else:
            raise ValueError('Incorrect value passed')
        
        return Response(password_serialized)
        
