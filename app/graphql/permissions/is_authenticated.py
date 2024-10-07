from typing import Any, Awaitable
from strawberry import Info
from strawberry.permission import BasePermission
from app.utils.jwtokens import JWTokens

class IsAuthenticated(BasePermission):
  message = "User is not authenticated"

  def has_permission(self, source: Any, info: Info[Any, Any], **kwargs: Any) -> bool | Awaitable[bool]:
    headers = info.context.request.headers
    if (not "Authorization" in headers): return False
    if (JWTokens.verify(headers["Authorization"])): return True