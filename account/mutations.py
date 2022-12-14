import graphene
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import token_auth
from graphql_jwt.mixins import ObtainJSONWebTokenMixin
from utils.mutations import FormMutation

from account.forms import SignupForm
from account.types import UserType


class SignUpMutation(ObtainJSONWebTokenMixin, FormMutation):
    class Meta:
        form_class = SignupForm

    user = graphene.Field(UserType)

    @classmethod
    def perform_mutate(cls, root, info, form):
        form.save()
        kwargs = {
            "password": form.data["password1"],
            get_user_model().USERNAME_FIELD: form.data[get_user_model().USERNAME_FIELD],
        }
        return cls.authorize_user(root, info, **kwargs)

    @classmethod
    @token_auth
    def authorize_user(cls, root, info, **kwargs):
        return cls.resolve(root, info, **kwargs)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)
