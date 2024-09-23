import strawberry
from typing import List
from app.services.user_service import UserService
from app.graphql.schema.user_types import UserType

@strawberry.type
class UserQuery:
  service = UserService()

  @strawberry.field
  def users(self) -> List[UserType]: 
    users = self.service.get_all_users()
    return [UserType(id=user.id, username=user.username, email=user.email) for user in users]