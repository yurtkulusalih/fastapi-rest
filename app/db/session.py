from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import AppSettings

settings = AppSettings()

def db_conn():
    engine = create_engine(
        settings.database_url
    )
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session()
    
def get_db():
    """
    Get SQLAlchemy database session
    """
    db = db_conn()
    try:
        yield db
    finally:
        db.close()
