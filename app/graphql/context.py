from typing import Dict, Any
from app.utils.jwtokens import JWTokens
from functools import cached_property
from strawberry.fastapi import BaseContext

class Context(BaseContext):
  
  @cached_property
  def user(self) -> Dict[str, Any]:
    return JWTokens.verify(self.request.headers.get("Auhtorization", None))
  
async def get_context() -> Context:
  return Context()