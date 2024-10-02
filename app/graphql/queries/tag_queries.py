import strawberry
from typing import List
from app.services.tag_service import TagService
from app.graphql.schema.tag_types import TagType

@strawberry.type
class TagQuery:

  @strawberry.field
  def tags(self) -> List[TagType]: 
    service = TagService()
    tags = service.get_all_tags()
    return [TagType(id=tag.id, name=tag.name) for tag in tags]