import strawberry
from typing import List
from app.services.tag_service import TagService
from app.graphql.schema.tag_types import TagType
from app.graphql.permissions.is_authenticated import IsAuthenticated

@strawberry.type
class TagQuery:

  @strawberry.field(permission_classes=[IsAuthenticated])
  def tags(self) -> List[TagType]: 
    service = TagService()
    tags = service.get_all_tags()
    return [TagType.from_orm(tag=tag) for tag in tags]