from typing import List
from sqlalchemy.orm import Session
from app.models.tag import Tag

class TagRepository:
  def __init__(self, db: Session) -> None:
    self.db = db

  def get_all_tags(self) -> List[Tag]:
    return self.db.query(Tag).all()
  
  def create_tag(self, tag: Tag) -> Tag:
    self.db.add(tag)
    self.db.commit()
    self.db.refresh(tag)
    return tag