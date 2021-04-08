from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """create a new user in system"""
    serializer_class = UserSerializer


