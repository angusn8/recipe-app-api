from rest_framework import serializers
from core.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('username', 'biography', 'photo')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = (
            'url',
            'email',
            'first_name',
            'last_name',
            'password',
            'profile'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.username = profile_data.get('username', profile.username)
        profile.biography = profile_data.get('biography', profile.biography)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance
