from app.environment import SECRET_KEY
from app.models.user import User
from jose import jwt

class JwtService:
  
  @staticmethod
  def encode(user: User) -> str:
    payload = { "user": user.id }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
  
  @staticmethod
  def decore(token: str):
    if (token is None): raise Exception("User is not authenticated")
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])