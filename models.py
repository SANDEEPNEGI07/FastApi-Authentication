from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext


Base = declarative_base()
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(Text, unique=True, index=True)
    email = Column(Text, unique=True, index=True)
    hasedh_password = Column(Text)
    role = Column(Text, default="user")


class Token(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    token = Column(Text, index=True)
    user_id = Column(Integer)
