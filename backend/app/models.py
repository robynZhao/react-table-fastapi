# Create SQLAlchemy models from the Base class
from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    # tells SQLAlchemy the name of the table to use in the database for each of these models
    __tablename__ = "users_react_fastAPI_table"

    # create all the model (class) attributes
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    website = Column(String, unique=True, index=True)
