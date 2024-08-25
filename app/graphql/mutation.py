import strawberry

from app.graphql.schema.user import UserType

from app.services.user_service import create_user

@strawberry.type
class Mutation:
  create_user: UserType = strawberry.mutation(resolver=create_user)