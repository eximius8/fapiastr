from dbutils.dbconnect import Base
from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from sqlalchemy.types import VARCHAR


class Dictionar(Base):
    """Dict model"""
    tname = Column('tname', VARCHAR(length=30), nullable=False)
    cname = Column('cname', VARCHAR(length=30), nullable=False)
    units = Column('units', Integer, nullable=True)

    __tablename__ = 'dictionary'
    __table_args__ = (
        PrimaryKeyConstraint(tname, cname),        
    )