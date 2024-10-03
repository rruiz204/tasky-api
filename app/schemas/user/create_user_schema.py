from pydantic import BaseModel, EmailStr, constr

class CreateUserSchena(BaseModel):
  username: str = constr(min_length=5, max_length=30)
  email: EmailStr
  password: str = constr(min_length=8)