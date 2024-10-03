from pydantic import BaseModel, EmailStr, constr

class LoginUserSchema(BaseModel):
  email: EmailStr
  password: str = constr(min_length=8)