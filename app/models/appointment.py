from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from app.db import Base
import enum

class AppointmentStatus( enum.Enum):
  pendiente = "pendiente"
  confirmado = "confirmado"
  cancelado = "cancelado"

class Appointment(Base):
  __tablename__= "appointments" 

  id = Column(Integer, primary_key=True)
  client_id = Column(Integer, ForeignKey("Users.id"))
  professional_id = Column(Integer, ForeignKey("Users.id"))
  service_id = Column(Integer, ForeignKey("service.id"))
  start_time = Column(DateTime)
  end_time = Column(DateTime)
  status = Column(Enum(AppointmentStatus), default=AppointmentStatus.pendiente)
