import strawberry
from app.services.auth_service import AuthService
from app.graphql.schema.auth_types import AuthTokenType, LoginUserInput

@strawberry.type
class AuthMutation:
  
  @strawberry.mutation
  def login_user(self, input: LoginUserInput) -> AuthTokenType:
    service = AuthService()
    token = service.login_user(input=input)
    return AuthTokenType.from_orm(token=token)