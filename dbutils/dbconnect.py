from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
import pyodbc
import os
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWD = os.getenv('PASSWD')
DBNAME = os.getenv('DBNAME')
COMPANY = os.getenv('COMPANY')
APPLICATION = os.getenv('APPLICATION')
SIGNATURE = os.getenv('SIGNATURE')

conn_str = f"sybase+pyodbc://{LOGIN}:{PASSWD}@{DBNAME}"

sybase = True

if sybase:
    engine = create_engine(conn_str, poolclass=NullPool)
else:
    engine = create_engine('postgresql+psycopg2://astraia:astraia@192.168.50.91/astraia-test')



Base = declarative_base(engine)



def loadSession():
    """Creating session for working with db"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session(bind=engine)
    if sybase:
        with engine.connect() as con:
            magicquery = f"SET TEMPORARY OPTION Connection_authentication='Company={COMPANY};Application={APPLICATION};Signature={SIGNATURE}'"
            statement = text(magicquery)
            con.execute(statement)
  
    return session