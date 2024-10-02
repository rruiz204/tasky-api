from typing import List
from app.database.unit_of_work import UnitOfWork
from app.graphql.schema.user_types import UserInput
from app.schemas.user.create_user_schema import CreateUserSchena
from app.models.user import User

class UserService:
  def __init__(self) -> None:
    self.uow = UnitOfWork()
  
  def get_all_users(self) -> List[User]:
    return self.uow.users.get_users();

  def create_new_user(self, input: UserInput) -> User:
    user = CreateUserSchena(**input.__dict__)
    return self.uow.users.create_user(User(username=user.username, email=user.email, password=user.password))