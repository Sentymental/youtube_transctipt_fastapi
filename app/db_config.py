"""
Module that contain our database configuration
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Load our environmental variables:
load_dotenv("../.env")

# Database URL:
SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]

# Create engine to the database:
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session, with scoped_session which will,
# create our registry of session factory.
db_sesion = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)

# Declarative base:
Base = declarative_base()
Base.query = db_sesion.query_property()
