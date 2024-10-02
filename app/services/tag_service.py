from typing import List
from app.database.unit_of_work import UnitOfWork
from app.graphql.schema.tag_types import CreateTagInput
from app.schemas.tag.create_tag_schema import CreateTagSchema
from app.models.tag import Tag

class TagService:
  def __init__(self) -> None:
    self.uow = UnitOfWork()

  def get_all_tags(self) -> List[Tag]:
    return self.uow.tags.get_all_tags()
  
  def create_new_tag(self, input: CreateTagInput) -> Tag:
    tag = CreateTagSchema(**input.__dict__)
    return self.uow.tags.create_tag(Tag(name=tag.name))