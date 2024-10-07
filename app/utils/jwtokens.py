from app.configuration.environment import SECRET_KEY
from jose import jwt
import datetime

class JWTokens:
  
  @staticmethod
  def generate(user_id: int) -> str:
    expiration = datetime.datetime.now() + datetime.timedelta(days=1)
    payload = { "id": user_id, "exp": expiration }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
  
  @staticmethod
  def verify(token: str):
    if (token is None): raise Exception("User is not authenticated")
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])