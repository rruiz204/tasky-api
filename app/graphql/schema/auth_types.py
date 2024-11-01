import strawberry

@strawberry.type
class AuthTokenType:
  type: str
  token: str

  @classmethod
  def from_orm(cls, token: str):
    return cls(token=token)

@strawberry.input
class LoginUserInput:
  email: str
  password: str