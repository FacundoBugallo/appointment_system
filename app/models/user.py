from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.db import Base
import enum #Importa el módulo enum para definir enumeraciones en Python.

class UserRole(enum.Enum):
  admin = "admin"
  staff = "staff"
  client = "client"
# Define una enumeración llamada UserRole con tres posibles valores: admin, staff y client.

class User(Base):
  __tablename__ = "Users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  hashed_password = Column(String)
  role = Column(Enum(UserRole), default=UserRole.client)
  is_activate = Column(Boolean, default=True)