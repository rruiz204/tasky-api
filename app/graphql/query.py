import strawberry

from typing import List

from app.graphql.schema.user import UserType

from app.services.user_service import get_all_users, get_specific_user, create_user

@strawberry.type
class Query:
  users: List[UserType] = strawberry.field(resolver=get_all_users)
  user: UserType = strawberry.field(resolver=get_specific_user)