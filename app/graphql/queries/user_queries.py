import strawberry
from typing import List
from app.graphql.schema.user_types import UserType
from app.use_cases.user.get_users.get_users_use_case import GetUsersUseCase
""" from app.graphql.permissions.is_authenticated import IsAuthenticated """
""" @strawberry.field(permission_classes=[IsAuthenticated]) """

@strawberry.type
class UserQuery:

  @strawberry.field
  def users(self) -> List[UserType]: 
    use_case = GetUsersUseCase()
    return use_case.execute()