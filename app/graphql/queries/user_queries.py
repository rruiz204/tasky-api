import strawberry
from typing import List
from app.database.unit_of_work import UnitOfWork
from app.graphql.schema.user_types import UserType
from app.use_cases.user.get_users.get_users_use_case import GetUsersUseCase
""" from app.graphql.permissions.is_authenticated import IsAuthenticated """
""" @strawberry.field(permission_classes=[IsAuthenticated]) """

@strawberry.type
class UserQuery:

  @strawberry.field
  def users(self) -> List[UserType]: 
    use_case = GetUsersUseCase()
    users = use_case.execute()
    return [UserType.from_orm(user=user) for user in users]