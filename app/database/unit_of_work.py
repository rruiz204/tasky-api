from app.database.db import get_db
from app.repositories.user_repository import UserRepository
from app.repositories.tag_repository import TagRepository

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
  
  @property
  def tags(self) -> TagRepository:
    if (self._tags is None):
      self._tags = TagRepository(self._db)
    return self._tags