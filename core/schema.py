import graphene
import graphql_jwt
from blog.schema import BlogMutation, BlogQuery
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required


# Auth Definitions
class UserType(DjangoObjectType):
    class Meta:
        model = User


class AuthQuery(graphene.ObjectType):
    user = graphene.Field(UserType)

    @login_required
    def resolve_user(self, info, **kwargs):
        return info.context.user


class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    revoke_token = graphql_jwt.Revoke.Field()
    delete_refresh = graphql_jwt.DeleteRefreshTokenCookie.Field()


# Root Schema Definitions
class Query(AuthQuery, BlogQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, BlogMutation, graphene.ObjectType):
    pass


RootSchema = graphene.Schema(query=Query, mutation=Mutation)
