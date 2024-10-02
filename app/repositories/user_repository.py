from typing import List
from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
  def __init__(self, db: Session) -> None:
    self.db = db

  def get_users(self) -> List[User]:
    return self.db.query(User).all()

  def create_user(self, user: User) -> User:
    self.db.add(user)
    self.db.commit()
    self.db.refresh(user)
    return user