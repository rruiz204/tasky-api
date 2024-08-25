import strawberry

@strawberry.type
class UserType:
  id: int
  username: str
  email: str
  password: str

@strawberry.input
class UserInput:
  username: str
  email: str
  password: str