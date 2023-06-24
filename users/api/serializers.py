from rest_framework.serializers import ModelSerializer
from users.models import User

class RegisterUserSerializer(ModelSerializer):
    class Meta():
        model = User
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.get('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance


class UserSerializer(ModelSerializer):
    class Meta():
        model =  User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class UserUpdateSerializer(ModelSerializer):
    class Meta():
        model =  User
        fields = ['first_name', 'last_name']