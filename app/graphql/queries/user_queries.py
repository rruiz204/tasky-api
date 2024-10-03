import strawberry
from typing import List
from app.services.user_service import UserService
from app.graphql.schema.user_types import UserType

@strawberry.type
class UserQuery:

  @strawberry.field
  def users(self) -> List[UserType]: 
    service = UserService()
    users = service.get_all_users()
    return [UserType.from_orm(user=user) for user in users]