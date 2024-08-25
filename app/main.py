from fastapi import FastAPI

app = FastAPI()

import strawberry
from strawberry.fastapi import GraphQLRouter
from app.graphql.query import Query
from app.graphql.mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, graphiql=True)

app.include_router(graphql_app, prefix="/graphql")