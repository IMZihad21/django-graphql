import graphene
from graphene_django import DjangoListField, DjangoObjectType
from graphql_jwt.decorators import login_required

from blog.models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post

    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_anonymous:
            return queryset.filter(is_active=True)
        return queryset


class Query(graphene.ObjectType):
    blog = graphene.Field(PostType, id=graphene.ID())
    all_blogs = DjangoListField(PostType)
    own_blogs = DjangoListField(PostType)

    def resolve_blog(self, info, id):
        return Post.objects.get(id=id)

    def resolve_all_blogs(self, info, **kwargs):
        return Post.objects.all()

    @login_required
    def resolve_own_blogs(self, info, **kwargs):
        return Post.objects.filter(id=info.context.user.id)
