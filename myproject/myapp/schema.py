
import graphene
from graphene_django import DjangoObjectType
from .models import Author

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)

    def resolve_all_authors(root, info):
        return Author.objects.all()

schema = graphene.Schema(query=Query)

