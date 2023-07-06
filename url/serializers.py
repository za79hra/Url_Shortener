from rest_framework import serializers
from .models import LinkShortenerModel


class SendOneTimePasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, min_length=11, required=True)

    def validate_phone_numbber(self, value: str) ->str:
        if not value.isnumeric() and len(value) != 11 and not value.startswhith('09'):
            raise serializers.ValidationError('invalid phone number')
        return value
    

class VerifyOneTimePasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, min_length=11, required=True)
    otp = serializers.CharField(max_length=4)

    def validate(self, attrs: str):
        if not(attrs['phone_number'].startswith('09') and attrs['phone_number'].isnumeric()):
            raise serializers.ValidationError('invalid phone number')
        if len(attrs['phone_number']) != 11:
            raise serializers.ValidationError("please  enter the correct phone number")

        
        if not(attrs['otp'].isnumeric()):
            raise serializers.ValidationError("otp in not valid")
        if len(attrs['otp']) != 4 :
            raise serializers.ValidationError("please  enter the correct code")
        return attrs
    


class LinkShortenerSerializer(serializers.ModelSerializer):
    short_url = serializers.ReadOnlyField()
    class Meta:
        model = LinkShortenerModel

        fields = ['orginal_url', 'short_url', 'url_viewed']
        read_only_fields = ['created_at', 'modified_at', 'is_deleted', 'owner']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['short_url'] = f"http://127.0.0.1:8000/{representation['short_url']}/"
        return representation

