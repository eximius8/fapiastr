from dbutils.dbconnect import Base
from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from sqlalchemy.types import VARCHAR, FLOAT


class Dictionar(Base):
    """Dict model"""
    tname = Column('tname', VARCHAR(length=30), nullable=False)
    cname = Column('cname', VARCHAR(length=30), nullable=False)
    dtype = Column('type', VARCHAR(length=2), nullable=False)
    enable = Column('enable', VARCHAR(length=255), nullable=False)

    defaultValue = Column('defaultvalue', VARCHAR(length=255), nullable=True)
    minimum = Column('minimum', FLOAT, nullable=True)
    maximum = Column('maximum', FLOAT, nullable=True)
    dlist = Column('list', VARCHAR(length=255), nullable=True)
    dnatip = Column('dna_tip', Integer, nullable=True)


    units = Column('units', Integer, nullable=True)

    __tablename__ = 'dictionary'
    __table_args__ = (
        PrimaryKeyConstraint(tname, cname),        
    )