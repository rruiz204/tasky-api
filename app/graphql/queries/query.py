import strawberry
from app.graphql.queries.user_queries import UserQuery

@strawberry.type
class Query(UserQuery):
  pass