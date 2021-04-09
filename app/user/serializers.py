from django.contrib.auth import get_user_model
from django.db import models

from psycopg2.extras import Json

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""
    interestings = serializers.ListField(child=serializers.CharField())
 #   languages = serializers.ListField(child=Json)


    class Meta:
        model = get_user_model()
       # fields = {'email', 'password', 'name', 'age', 'languages', 'interestings'}
        fields = ('email', 'password', 'name', 'age', 'interestings', 'languages')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}


    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

