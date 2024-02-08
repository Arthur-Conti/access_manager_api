from rest_framework import serializers

from access import Access


class AccessSerializer(serializers.Serializer):

    class Meta:
        model = Access
        fields = ['title', 'username', 'password', 'url', 'notes']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')

        if request.method and 'id' in request.parser_context['kwargs']:
            return data
        else:
            data.pop('password', None)
            return data
        
    def create(self, user_id, validated_data):
        access = Access(
            user_id=user_id, 
            title=validated_data.get('title'), 
            username=validated_data.get('username'), 
            password=validated_data('password'), 
            url=validated_data('url'), 
            notes=validated_data('notes')
        )
        access.save()

        return access
