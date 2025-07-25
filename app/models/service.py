from sqlalchemy import Column, Integer, String, Float
from app.db import Base

class Service(Base):
  __tablename__ = "service"
  
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(50), index=True)
  duration_minutes = Column(Integer)
  price = Column(Float)