from rest_framework import serializers
from profiles_api import models
class HelloSerializer(serializers.Serializer):
    """Serializa un campo para probar nuestro APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializa objeto de perfil de usuario"""

    class Meta:
        model= models.UserProfile
        fields=('id','email','name','password', 'avatar')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Crea y retorna nuevo usuario"""
        user=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            avatar=validated_data['avatar'],
        )
        return user

    def update(self,instance, validated_data):
        """Handle upating user account"""
        if 'password' in validated_data:
            password= validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializador de profile feed item"""
    class Meta:
        model=models.ProfileFeedItem
        fields=('id','user_profile', 'status_text','created_on')
        extra_kwargs={'user_profile':{'read_only':True}}

