from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    id  = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
        )
        if validated_data.get('password') is not None:
            user.set_password(validated_data.get('password'))

        user.save()

        return user
