from pydantic import BaseModel, constr

class CreateTagSchema(BaseModel):
  name: constr(min_length=3)