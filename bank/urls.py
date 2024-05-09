from django.urls import path
from graphene_django.views import GraphQLView
from bank.schema import schema
from .views import insert_data, welcome

urlpatterns = [
    # Only a single URL to access GraphQL
    path("", welcome),
    path("insertData", insert_data ),
    path("gql", GraphQLView.as_view(graphiql=True, schema=schema)),
]