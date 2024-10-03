from pydantic import BaseModel, constr

class CreateTagSchema(BaseModel):
  name: str = constr(min_length=3)