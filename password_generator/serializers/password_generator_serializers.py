from rest_framework import serializers

from core.pass_generator_api.random_pass_generator import RandomPassGenerator


class PasswordGeneratorSerializer(serializers.Serializer):
    password = serializers.CharField()


class PostPasswordGeneratorSerializer(serializers.Serializer):
    length = serializers.CharField()
    numbers = serializers.BooleanField()
    special = serializers.BooleanField()
    uppercase = serializers.BooleanField()
    lowercase = serializers.BooleanField()

    def create(self, validated_data):
        length = validated_data.get('length')
        numbers = validated_data.get('numbers')
        special = validated_data.get('special')
        uppercase = validated_data.get('uppercase')
        lowercase = validated_data.get('lowercase')

        pass_generator = RandomPassGenerator(length, numbers, special, uppercase, lowercase)

        password = pass_generator.generate_password()

        return password
