from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__default_rounds=12)

class HasherService:

  @staticmethod
  def hash(password: str) -> str:
    return pwd_context.hash(password)
  
  @staticmethod
  def verify(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)