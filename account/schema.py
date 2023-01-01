import graphene
import graphql_jwt
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from account.models import User
from account.mutations import SignUpMutation
from account.types import UserType


# Auth Definitions
class AuthQuery(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.ID(default_value=None))

    @login_required
    def resolve_user(self, info, **kwargs):
        user_id = kwargs["id"]
        if user_id is None:
            return info.context.user
        if not info.context.user.is_staff:
            raise GraphQLError("You do not have permission to view other users")
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist as e:
            raise GraphQLError(f"No user not found with id {user_id}!") from e


# Mutations


class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    sign_up = SignUpMutation.Field()
