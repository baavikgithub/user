from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class Userserializer(serializers.modelserializer):
   class Meta:
       model=User
       fields=['id','email','username']
class Registerserializer(serializers.Modelserializer):
    class Meta:
        model=User
        fields=['id','email','username']
        extra_kwargs = {'password': {'write_only': True}}
def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'].lower(),
            password=validated_data['password']
        )
        return user
class Loginserializer(serializers.Modelserializer):
    email=serializers.EmailField()
    password=serializers.CharField()
def validate(self, data):
    user =authenticate(**data)
    if user and user.is_active:
        return user
        raise serializers.ValidationError("Invalid Credentials")