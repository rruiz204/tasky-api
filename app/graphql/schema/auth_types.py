import strawberry

@strawberry.type
class AuthTokenType:
  type: str
  token: str

@strawberry.input
class LoginUserInput:
  email: str
  password: str