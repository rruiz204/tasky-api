import strawberry
from datetime import datetime

@strawberry.type
class TagType:
  id: int
  name: str

@strawberry.input
class CreateTagInput:
  name: str