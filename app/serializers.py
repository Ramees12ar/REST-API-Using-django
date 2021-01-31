from rest_framework import serializers
from app.models import users

class usersData(serializers.ModelSerializer):
    class Meta:
        model=users
        fields=('__all__')
