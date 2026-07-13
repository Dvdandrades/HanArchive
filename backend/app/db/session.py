from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

engine = create_engine(f"postgresql+psycopg2://{settings.postgres_user}:{settings.postgres_pw}@localhost:5432/hanarchivedb")

Session = sessionmaker(autoflush=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()