from sqlalchemy import Column, Integer, Datatime, ForeignKey, Enum
from app.db import Base

class AppointmentStatus(enum.Enum):
  pendiente = "pendiente"
  confirmado = "confirmado"
  cancelado = "cancelado"

class Appointment(base):
  __tablename_ = "appointments" 

  id
  client_id
  professional_id
  service_id
  start_time
  end_time
  status
