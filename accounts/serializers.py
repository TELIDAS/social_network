from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

User = get_user_model()


class NPOObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(NPOObtainPairSerializer, cls).get_token(user)

        token["username"] = user.username
        return token


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "last_login",
        )


class UserDuplicateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
        )


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
        )

        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def validate_username(self, value):
        data = self.get_initial()
        username = data.get("username")
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            duplicate_obj = User.objects.get(username=username)
            serializer = UserDuplicateSerializer(duplicate_obj)
            raise ValidationError(
                "This username has been registered!" + str(serializer.data)
            )
        else:
            pass
        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        make_password(password=validated_data["password"])

        user.set_password(validated_data["password"])
        user.save()

        return user
