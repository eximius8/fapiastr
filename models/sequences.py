from dbutils.dbconnect import Base
from sqlalchemy import Column, Integer, SmallInteger, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.types import VARCHAR, BOOLEAN
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column



class SequenceData(Base):

    sequence = Column('sequence', Integer, nullable=False)
    block = Column('block', Integer, nullable=False)

    n = Column('n', SmallInteger, nullable=False)

    __tablename__ = 'SequenceData'
    __table_args__ = (
        PrimaryKeyConstraint(sequence, block), 
    )


class Sequence(Base):

    id = Column('id', Integer, nullable=False)
    setname = Column('setname', VARCHAR(length=20), nullable=False)

    parent = Column('parent', Integer, nullable=True)
    hide = Column('hide', BOOLEAN, nullable=True)
    dna: Mapped[int] = mapped_column(ForeignKey("Lang.DNA")) #Column('dna', Integer, nullable=True)
    expand = Column('expand', BOOLEAN, nullable=True)
    datavalue = Column('datavalue', VARCHAR(length=60), nullable=False)
    enabled = Column('enabled', VARCHAR(length=255), nullable=False)
    summary = Column('summary', VARCHAR(length=2048), nullable=False)
    keep = Column('keep', SmallInteger, nullable=True)
    licensed = Column('license', VARCHAR(length=20), nullable=False)
    control = Column('control', VARCHAR(length=255), nullable=False)
    sset = Column('sset', VARCHAR(length=3), nullable=False)

    __tablename__ = 'Sequences'
    __table_args__ = (
        PrimaryKeyConstraint(id, setname),
    )