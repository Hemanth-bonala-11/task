import graphene
from graphene_django import DjangoObjectType
from .models import Bank

class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        fields = "__all__"

class Query(graphene.ObjectType):
    all_banks = graphene.List(BankType, first=graphene.Int(), after=graphene.String(),  before=graphene.String(), ifsc=graphene.String(),
                              bank_id=graphene.Int())

    def resolve_all_banks(self, info, first=None,  bank_id=None, ifsc=None):
        queryset = Bank.objects.all()


        if bank_id:
            queryset = queryset.filter(bank_id=bank_id)
        if ifsc:
            queryset = queryset.filter(ifsc=ifsc)

        if first:
            queryset = queryset[:first]

        return queryset

schema = graphene.Schema(query=Query)