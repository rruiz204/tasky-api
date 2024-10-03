import strawberry
from app.models.tag import Tag

@strawberry.type
class TagType:
  id: int
  name: str

  @classmethod
  def from_orm(cls, tag: Tag):
    return cls(id=tag.id, name=tag.name)

@strawberry.input
class CreateTagInput:
  name: str