import strawberry
from app.graphql.queries.user_queries import UserQuery
from app.graphql.queries.tag_queries import TagQuery

@strawberry.type
class Query(UserQuery, TagQuery):
  pass