from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cambia esto por tus credenciales reales
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:tu_clave@localhost:5432/glasslab"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia que usarás en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
