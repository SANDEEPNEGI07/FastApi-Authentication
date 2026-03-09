from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import PostgresDsn
from config import setting


engine = create_engine()
Base = declarative_base()

database_url = PostgresDsn.build(
    scheme="postgresql",
    user = setting.db_user,
    password = setting.db_password,
    host = setting.db_host,
    path = f"/{setting.db_name}"
)

SQLALCHEMY_DATABASE_URL = str(database_url)
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit= False,
    bind = engine
)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
