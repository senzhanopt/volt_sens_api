import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def get_session():
    """
    Provides a SQLAlchemy Session for FastAPI dependency injection.
    """
    session = Session()
    try:
        yield session
    finally:
        session.close()
