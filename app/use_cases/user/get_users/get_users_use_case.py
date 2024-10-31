from app.database.unit_of_work import UnitOfWork
from app.models.user import User
from typing import List

class GetUsersUseCase:
  def __init__(self):
    self.unitOfWork = UnitOfWork()

  def execute(self) -> List[User]:
    return self.unitOfWork.users.get_users()