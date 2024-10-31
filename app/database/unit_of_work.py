from app.database.context import get_db
from app.repositories.user_repository import UserRepository

class UnitOfWork:
  def __init__(self):
    self._db = next(get_db())

    self._users = None
    self._tags = None
  
  @property
  def users(self) -> UserRepository:
    if (self._users is None):
      self._users = UserRepository(self._db)
    return self._users