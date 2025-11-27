from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Corrected URL (no leading space)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Creating the engine (connection to SQLite DB)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}    # required for SQLite
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for ORM models
Base = declarative_base()

 #connect_args is specific to SQLite to allow the use of the same connection in different threads
#declarative_base is a base class for all ORM models to inherit from 


#sessionmaker is a factory for creating new Session objects
#autocommit=False means changes are not saved until explicitly committed
#autoflush=False means changes are not sent to the database until committed
#bind=engine links the session to the database engine

