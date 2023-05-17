from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connect to SQLite
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# Connect to PostgreSQL
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:test1234!@localhost/TodoApplicationDatabase'
SQLALCHEMY_DATABASE_URL = 'postgresql://addnysdm:L7rbJqKRCnKtrPUPZydP5yf3wqoQjBDb@mahmud.db.elephantsql.com/addnysdm'
# this line is for SQLite only
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# for postgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
