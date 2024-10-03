import strawberry
from app.services.tag_service import TagService
from app.graphql.schema.tag_types import TagType, CreateTagInput

@strawberry.type
class TagMutation():

  @strawberry.mutation
  def create_tag(self, input: CreateTagInput) -> TagType:
    service = TagService()
    tag = service.create_new_tag(input=input)
    return TagType.from_orm(tag=tag)