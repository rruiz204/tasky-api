from app.database.unit_of_work import UnitOfWork
from app.graphql.schema.auth_types import LoginUserInput, AuthTokenType
from app.use_cases.authentication.login_user.login_user_schema import LoginUserSchema
from app.services.hasher_service import HasherService
from app.services.jwt_service import JwtService
from app.models.user import User

class LoginUserUseCase:
  def __init__(self):
    self.unitOfWork = UnitOfWork()

  def execute(self, input: LoginUserInput) -> AuthTokenType:
    validated = LoginUserSchema(**input.__dict__)
    user = self.unitOfWork.users.find_user(User.email == validated.email)

    if (user is None): raise Exception("user not found")

    if (not HasherService.verify(validated.password, user.password)):
      raise Exception("invalid credentials")
    
    token = JwtService.encode(user=user)
    return AuthTokenType(type="Bearer", token=token)