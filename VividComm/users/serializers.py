from rest_framework import serializers
from .models import CustomUser # Import your CustomUser model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # Fields that will be included in the API response for user details and registration input
        fields = ('id', 'username', 'email', 'phone_number', 'profile_picture', 'bio', 'password')
        # password should only be writeable (for registration/update), not readable in API response
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Override the create method to ensure the password is hashed properly
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'), # Use .get() as email might be optional
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number'),
            bio=validated_data.get('bio'),
            profile_picture=validated_data.get('profile_picture')
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'profile_picture', 'bio', 'date_joined']
        read_only_fields = ['username', 'email', 'date_joined']