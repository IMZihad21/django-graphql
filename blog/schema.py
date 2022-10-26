import graphene
from graphene_django import DjangoListField
from graphql_jwt.decorators import login_required
from utils.mutations import DjangoMutationForm

from blog.forms import PostForm
from blog.models import Post
from blog.types import PostType


# Query
class BlogQuery(graphene.ObjectType):
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


# Mutation


class CreateBlog(DjangoMutationForm):
    blog = graphene.Field(PostType)

    class Meta:
        form_class = PostForm
        return_field_name = "blog"

    @classmethod
    @login_required
    def perform_mutate(cls, form, info):
        form.instance.author = info.context.user
        return super().perform_mutate(form, info)


class BlogMutation(graphene.ObjectType):
    create_blog = CreateBlog.Field()
