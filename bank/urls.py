from django.urls import path
from graphene_django.views import GraphQLView
from bank.schema import schema
from .views import insert_data

urlpatterns = [
    # Only a single URL to access GraphQL
    path("insertData", insert_data ),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]