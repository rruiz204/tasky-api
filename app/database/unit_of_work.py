from app.database.db import get_db
from app.repositories.user_repository import UserRepository

class UnitOfWork:
  
  def __init__(self):
    self._db = next(get_db())

    self._users = None
  
  @property
  def users(self):
    if (self._users is None):
      self._users = UserRepository(self._db)
    return self._users