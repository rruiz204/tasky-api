import strawberry
from app.graphql.schema.user_types import UserType, CreateUserInput
from app.use_cases.user.create_user.create_user_use_case import CreateUserUseCase

@strawberry.type
class UserMutation():

  @strawberry.mutation
  def create_user(self, input: CreateUserInput) -> UserType:
    use_case = CreateUserUseCase()
    user = use_case.execute(input=input)
    return UserType.from_orm(user=user)