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

LOGIN = os.getenv('LOGIN', 'dba')
PASSWD = os.getenv('PASSWD', 'soot')
DBNAME = os.getenv('DBNAME', 'astraia-dev')
COMPANY = os.getenv('COMPANY', 'Astraia Software GmbH')
APPLICATION = os.getenv('APPLICATION', 'astraia')
SIGNATURE = os.getenv('SIGNATURE', '000fa55157edb8e14d818eb4fe3db41447146f1571g41642fefdd31cdd001026203dbcafb69fc384292')

conn_str = f"sybase+pyodbc://{LOGIN}:{PASSWD}@{DBNAME}"


engine = create_engine(conn_str, poolclass=NullPool)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base(engine)



def loadSession():
    """Creating session for working with db"""

    Session = sessionmaker(bind=engine)
    session = Session(bind=engine)    
    with engine.connect() as con:
        magicquery = f"SET TEMPORARY OPTION Connection_authentication='Company={COMPANY};Application={APPLICATION};Signature={SIGNATURE}'"
        statement = text(magicquery)
        con.execute(statement)
  
    return session

# Dependency
def get_db():
    db = SessionLocal()
      
    with engine.connect() as con:
        magicquery = f"SET TEMPORARY OPTION Connection_authentication='Company={COMPANY};Application={APPLICATION};Signature={SIGNATURE}'"
        statement = text(magicquery)
        con.execute(statement)
    try:
        yield db
    finally:
        db.close()