import strawberry
from app.models.user import User

@strawberry.type
class UserType:
  id: int
  username: str
  email: str

@strawberry.input
class CreateUserInput:
  username: str
  email: str
  password: str