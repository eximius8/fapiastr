from sqlalchemy import  Column, Integer
from sqlalchemy.types import VARCHAR
from dbutils.dbconnect import Base


class LangObject(Base):
    """Language model"""
    DNA = Column('DNA', Integer, primary_key=True, autoincrement=True)
    En = Column('En', VARCHAR(length=4), nullable=True)
    Fr = Column('Fr', VARCHAR(length=4), nullable=True)
    Nl = Column('Nl', VARCHAR(length=4), nullable=True)
    De = Column('De', VARCHAR(length=4), nullable=True)
    It = Column('It', VARCHAR(length=4), nullable=True)
    Pt = Column('Pt', VARCHAR(length=4), nullable=True)
    Es = Column('Es', VARCHAR(length=4), nullable=True)
    NL_be = Column('NL_be', VARCHAR(length=4), nullable=True)
    Fi = Column('Fi', VARCHAR(length=4), nullable=True)
    Da = Column('Da', VARCHAR(length=4), nullable=True)
    pl = Column('pl', VARCHAR(length=4), nullable=True)
    Cs = Column('Cs', VARCHAR(length=4), nullable=True)
    El = Column('El', VARCHAR(length=4), nullable=True)
    Tr = Column('Tr', VARCHAR(length=4), nullable=True)
    Pt_br = Column('Pt_br', VARCHAR(length=4), nullable=True)
    Ro = Column('Ro', VARCHAR(length=4), nullable=True)
    Hu = Column('Hu', VARCHAR(length=4), nullable=True)
    Fr_ch = Column('Fr_ch', VARCHAR(length=4), nullable=True)
    De_ch = Column('De_ch', VARCHAR(length=4), nullable=True)
    Sv = Column('Sv', VARCHAR(length=4), nullable=True)
    Zh = Column('Zh', VARCHAR(length=4), nullable=True)
    Bg = Column('Bg', VARCHAR(length=4), nullable=True)
    Ru = Column('Ru', VARCHAR(length=4), nullable=True)
    Uk = Column('Uk', VARCHAR(length=4), nullable=True)
    Sr = Column('Sr', VARCHAR(length=4), nullable=True)
    Ja = Column('Ja', VARCHAR(length=4), nullable=True)
    Sq = Column('Sq', VARCHAR(length=4), nullable=True)
    Vi = Column('Vi', VARCHAR(length=4), nullable=True)
    Fr_ca = Column('Fr_ca', VARCHAR(length=4), nullable=True)
    Sk = Column('Sk', VARCHAR(length=4), nullable=True)
    Iw = Column('Iw', VARCHAR(length=4), nullable=True)
    ko = Column('ko', VARCHAR(length=4), nullable=True)
    En_ca = Column('En_ca', VARCHAR(length=4), nullable=True)
    Zh_tw = Column('Zh_tw', VARCHAR(length=4), nullable=True)
    No = Column('No', VARCHAR(length=4), nullable=True)
    Lv = Column('Lv', VARCHAR(length=4), nullable=True)
    Et = Column('Et', VARCHAR(length=4), nullable=True)
       
    __tablename__ = 'Lang'
