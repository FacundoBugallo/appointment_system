from sqlalchemy import Column, Integer, Datatime, ForeignKey, Enum
from app.db import Base

class AppointmentStatus(enum.Enum):
  pendiente = "pendiente"
  confirmado = "confirmado"
  cancelado = "cancelado"

class Appointment(base):
  __tablename_ = "appointments" 

  id = Column(Integer, primary_key=True)
  client_id = Column(Integer, ForeignKey("Users.id"))
  professional_id = Column(Integer, ForeignKey("Users.id"))
  service_id = Column(Integer, ForeignKey("services.id"))
  start_time = Column(Datatime)
  end_time = Column(Datatime)
  status = Column(Enum(AppointmentStatus), default=AppointmentStatus.pendiente)
