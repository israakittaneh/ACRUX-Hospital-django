from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from doctor.serializers import DoctorSerializer
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')

class UserSerialize(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id' ,'email' , 'name','doctor')