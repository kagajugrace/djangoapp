from rest_framework import routers, serializers, viewsets
from .models import *
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        #depth=1
        fields=('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')
        extra_kwargs = {'user': {'required': False}}

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields =('username','password', 'email', 'profile', 'first_name','last_name')
        

    def create(self, validated_data):

        # create user 
        insert = User.objects.create(
           
            email = validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']),

            first_name=validated_data['first_name'],
            last_name =validated_data['last_name']
            # etc ...
        )

        profile_data = validated_data.pop('profile')
        # create profile
        profile = Profile.objects.create(
            user =insert,
            username =profile_data['username'],
            country = profile_data['country'],
            accounttype = profile_data['accounttype'],
            gender = profile_data['gender']
            # etc...
        )

        return insert