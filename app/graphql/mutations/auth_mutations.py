import strawberry
from app.graphql.schema.auth_types import LoginUserInput, AuthTokenType
from app.use_cases.authentication.login_user.login_user_use_case import LoginUserUseCase

@strawberry.type
class AuthMutation:
  
  @strawberry.mutation
  def login_user(self, input: LoginUserInput) -> AuthTokenType:
    use_case = LoginUserUseCase()
    return use_case.execute(input=input)