from rest_framework import serializers
from accounts.models import CustomUser

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role')
