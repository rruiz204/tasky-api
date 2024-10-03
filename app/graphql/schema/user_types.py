import strawberry
from app.models.user import User

@strawberry.type
class UserType:
  id: int
  username: str
  email: str

  @classmethod
  def from_orm(cls, user: User):
    return cls(id=user.id, username=user.username, email=user.email)

@strawberry.input
class CreateUserInput:
  username: str
  email: str
  password: str