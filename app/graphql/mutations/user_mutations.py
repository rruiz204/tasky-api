import strawberry
from app.services.user_service import UserService
from app.graphql.schema.user_types import UserType, CreateUserInput

@strawberry.type
class UserMutation():

  @strawberry.mutation
  def create_user(self, input: CreateUserInput) -> UserType:
    service = UserService()
    user = service.create_new_user(input=input)
    return UserType.from_orm(user=user)