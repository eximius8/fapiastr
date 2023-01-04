from dbutils.dbconnect import Base
from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from sqlalchemy.types import VARCHAR, FLOAT, BOOLEAN, SMALLINT


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
    zeroallowed = Column('zeroallowed', BOOLEAN, nullable=True)
    required = Column('required', BOOLEAN, nullable=True)
    anomaly = Column('anomaly', BOOLEAN, nullable=True)
    length = Column('length', SMALLINT, nullable=True)
    global_prop = Column('global', BOOLEAN, nullable=True)
    dna = Column('dna', Integer, nullable=True)
    dna_chart = Column('dna_chart', Integer, nullable=True)
    minvalue = Column('minvalue', FLOAT, nullable=True)
    maxvalue = Column('maxvalue', FLOAT, nullable=True)
    special = Column('special', SMALLINT, nullable=True)
    units = Column('units', Integer, nullable=True)
    flagged = Column('flagged', BOOLEAN, nullable=True)
    dna_flag = Column('dna_flag', Integer, nullable=True)
    flag_expression = Column('flag_expression', VARCHAR(length=2000), nullable=True)
    blocks = Column('blocks', VARCHAR(length=255), nullable=True)
    block_multi = Column('block_multi', BOOLEAN, nullable=True)
    flag_link = Column('flag_link', VARCHAR(length=255), nullable=True)
    int_precision = Column('int_precision', SMALLINT, nullable=True)
    dec_precision = Column('dec_precision', SMALLINT, nullable=True)
    existing_value_changeable = Column('existing_value_changeable', VARCHAR(length=512), nullable=True)

    __tablename__ = 'dictionary'
    __table_args__ = (
        PrimaryKeyConstraint(tname, cname),        
    )