from app.database.unit_of_work import UnitOfWork
from app.graphql.schema.auth_types import LoginUserInput
from app.schemas.auth.login_user_schema import LoginUserSchema
from app.models.user import User
from app.utils.jwtokens import JWTokens
from app.utils.hasher import Hasher

class AuthService:
  def __init__(self) -> None:
    self.uow = UnitOfWork()

  def login_user(self, input: LoginUserInput) -> str:
    validated = LoginUserSchema(**input.__dict__)
    user = self.uow.users.find_user(User.email == validated.email)

    if (user is None): raise Exception("User not found")
    if (not Hasher.verify(validated.password, user.password)): raise Exception("Invalid credentials")
    return JWTokens.generate(user_id=user.id)