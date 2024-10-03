from jose import jwt
import datetime

from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

class JWTokens:
  
  @staticmethod
  def generate(user_id: int) -> str:
    expiration = datetime.datetime.now() + datetime.timedelta(days=1)
    payload = { "id": user_id, "exp": expiration }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
  
  @staticmethod
  def verify(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload