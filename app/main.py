from fastapi import FastAPI

app = FastAPI()

# Rest API
""" @app.get("/")
async def root():
  return { "message": "Hello World!" } """

import strawberry
from strawberry.fastapi import GraphQLRouter

# GrpahQL API
@strawberry.type
class Query:

  @strawberry.field
  def testing(self) -> str:
    return "Hello World!"

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")