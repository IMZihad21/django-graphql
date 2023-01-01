from graphene_django import DjangoObjectType

from account.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_superuser",
            "date_joined",
            "last_login",
        )
