from pydantic import BaseModel, EmailStr, constr

class UserInputModel(BaseModel):
  username: constr(min_length=3, max_length=50)
  email: EmailStr
  password: constr(min_length=8)