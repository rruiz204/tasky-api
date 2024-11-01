from app.database.unit_of_work import UnitOfWork
from app.graphql.schema.user_types import UserType
from typing import List

class GetUsersUseCase:
  def __init__(self):
    self.unitOfWork = UnitOfWork()

  def execute(self) -> List[UserType]:
    users = self.unitOfWork.users.get_users()
    return [UserType(
      id=user.id,
      username=user.email,
      email=user.email
    ) for user in users]