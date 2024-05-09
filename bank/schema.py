import graphene
from graphene_django import DjangoObjectType
from .models import Bank

class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        fields = "__all__"

class Query(graphene.ObjectType):
    all_banks = graphene.List(BankType, first=graphene.Int(), after=graphene.String(), last=graphene.Int(), before=graphene.String())

    def resolve_all_banks(self, info, first=None, after=None, last=None, before=None):
        queryset = Bank.objects.all()
        if first:
            queryset = queryset[:first]
        elif last:
            queryset = queryset[-last:]
        elif after:
            queryset = queryset.filter(id__gt=after)
        elif before:
            queryset = queryset.filter(id__lt=before)
        return queryset

schema = graphene.Schema(query=Query)