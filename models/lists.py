from dbutils.dbconnect import Base
from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from sqlalchemy.types import VARCHAR, BOOLEAN, SMALLINT


class Listobject(Base):
    """Dict model"""
    id = Column('id', Integer, nullable=False)
    listname = Column('listname', VARCHAR(length=50), nullable=False)
    version = Column('version', SMALLINT, nullable=False)
    
    defaultitem = Column('defaultitem', BOOLEAN, nullable=True)
    alert = Column('alert', BOOLEAN, nullable=True)
    dna = Column('dna', Integer, nullable=True)
    lorder = Column('lorder', Integer, nullable=True)
    child = Column('child', VARCHAR, nullable=True)
    deleted = Column('deleted', BOOLEAN, nullable=True)
    associated = Column('associated', VARCHAR(length=30), nullable=True)
    department = Column('department', VARCHAR(length=255), nullable=True)
    tag = Column('tag', VARCHAR(length=10), nullable=True)
    issue = Column('issue', VARCHAR(length=20), nullable=True)
    parenttext = Column('parenttext', BOOLEAN, nullable=True)

  
    __tablename__ = 'lists'
    __table_args__ = (
        PrimaryKeyConstraint(id, listname, version),        
    )