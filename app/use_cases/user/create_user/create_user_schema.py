from pydantic import BaseModel, EmailStr, Field

class CreateUserSchena(BaseModel):
  username: str = Field(min_length=5, max_length=30)
  email: EmailStr
  password: str = Field(min_length=8, max_length=50)