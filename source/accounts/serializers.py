from rest_framework import serializers

from accounts.models import CustomUser


class CustomUserSignUpSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = '__all__'

    def save(self, *args,**kwargs):
        password = self.validated_data.pop('password')
        repeat_password = self.validated_data.pop('repeat_password')

        if password != repeat_password:
            raise serializers.ValidationError({'Error': 'Passwords does not match.'})

        if CustomUser.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError({'Error': 'Email already exists'})

        account = CustomUser(email=self.validated_data["email"], username=self.validated_data["username"])
        account.set_password(password)
        account.save()
        return account


class CustomUserSignInSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'password']