from sqlalchemy import Column, String, Integer, DateTime
from app.database.context import Base
from sqlalchemy.sql import func

class Tag(Base):
  __tablename__ = "tags"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())