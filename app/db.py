from sqlalchemy import create_engine #_Crear el motor para conectar la base de datos
from sqlalchemy.orm import sessionmaker, declarative_base 
#Sessionmaker crea las seciones par alinteracctuar con la base de datos
#declarative_base Permite definir clases modelo (tablas) usando la sintaxis de SQLAlchemy.
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#es una fábrica de sesiones para interactuar con la base de datos.
# Autocommit=False: Las transacciones no se confirman automáticamente.
# Autoflush=False: Los cambios no se envían automáticamente a la base de datos.
# Bind=engine: Usa el motor creado anteriormente.
Base = declarative_base()

# Este archivo prepara todo lo necesario para conectar y trabajar con la base de datos usando SQLAlchemy en el proyecto
