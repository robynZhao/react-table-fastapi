# import SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database URL for SQLAlchemy
# "connecting" to a SQLite database (opening a file with the SQLite database) => only allow one thread to communicate with
# The file will be located at the same directory in the file app.db.
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# create a SQLAlchemy "engine"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


# Each instance (the actual database session) of the SessionLocal class will be a database session
# Handling Threading Issues
# sessionmaker: initial new session objects & check out a connection
# Sessionmaker initializes these sessions by requesting a connection from the engine's connection pool
# and attaching a connection to the new Session object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy’s declarative_base() and Base.metadata.create_all()
# allows users to write just one class per table to use in the app
# declarative_base() base class returns a class & contains a MetaData object where newly defined Table objects are collected
# This MetaData object is accessed when we call the line models.Base.metadata.create_all()to create all of our tables
Base = declarative_base()

