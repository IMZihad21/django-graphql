import graphene
from blog.schema import BlogMutation, BlogQuery
from users.schema import AuthMutation, AuthQuery


# Root Schema Definitions
class Query(AuthQuery, BlogQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, BlogMutation, graphene.ObjectType):
    pass


RootSchema = graphene.Schema(query=Query, mutation=Mutation)
