from sqlalchemy import Column, String, Integer, DateTime
from app.database.db import Base
from sqlalchemy.sql import func

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, nullable=False)
  email = Column(String, nullable=False, index=True)
  password = Column(String, nullable=False)
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())