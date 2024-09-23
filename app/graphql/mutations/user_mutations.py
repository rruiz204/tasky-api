import strawberry
from app.services.user_service import UserService
from app.graphql.schema.user_types import UserType, UserInput


@strawberry.type
class UserMutation():
  service = UserService()

  @strawberry.mutation
  def create_user(self, input: UserInput) -> UserType:
    user = self.service.create_new_user(input=input)
    return UserType(id=user.id, username=user.username, email=user.email)