from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model

CustomUser = get_user_model()
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email','password']
        extra_kwargs = {'password':{'write_only':True}}
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password =  serializers.CharField(write_only=True)
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username , password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        data["user"] = user
        return data