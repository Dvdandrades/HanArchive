from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost:5432/hanarchivedb")

Session = sessionmaker(autoflush=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()