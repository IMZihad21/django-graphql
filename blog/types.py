from graphene_django import DjangoObjectType

from blog.models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post

    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_anonymous:
            return queryset.filter(is_active=True)
        return queryset
