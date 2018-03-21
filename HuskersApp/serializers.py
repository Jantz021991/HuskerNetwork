from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ('name', 'address_line_1', 'address_line_2', 'city', 'state', 'country')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name', 'venue', 'meeting_time', 'groupAdmin', 'hashtag', 'users')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('post_text', 'group', 'user')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class PlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)

    class Meta:
        model = Player
        fields = ('users', 'date_of_birth', 'favorite_team', 'current_location', 'introduction')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        player = Player.objects.create(user=user, **validated_data)
        return player
