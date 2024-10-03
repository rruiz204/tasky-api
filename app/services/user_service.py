from typing import List
from app.database.unit_of_work import UnitOfWork
from app.graphql.schema.user_types import CreateUserInput
from app.schemas.user.create_user_schema import CreateUserSchena
from app.models.user import User
from app.utils.hasher import Hasher

class UserService:
  def __init__(self) -> None:
    self.uow = UnitOfWork()
  
  def get_all_users(self) -> List[User]:
    return self.uow.users.get_users();

  def create_new_user(self, input: CreateUserInput) -> User:
    validated_user = CreateUserSchena(**input.__dict__)
    validated_user.password = Hasher.hash(validated_user.password)
    return self.uow.users.create_user(User(**validated_user.model_dump()))