import graphene
import graphql_jwt
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    revoke_token = graphql_jwt.Revoke.Field()

    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

    viewer = graphene.Field(UserType)

    @login_required
    def resolve_viewer(self, info, **kwargs):
        return info.context.user


schema = graphene.Schema(query=Query, mutation=Mutation)
