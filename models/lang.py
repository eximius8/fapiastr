from sqlalchemy import  Column, Integer
from sqlalchemy.types import VARCHAR
from dbutils.dbconnect import Base


class LangObject(Base):
    """Language model"""
    dna = Column('DNA', Integer, primary_key=True, autoincrement=True)
    en = Column('En', VARCHAR(length=4), nullable=True)
    fr = Column('Fr', VARCHAR(length=4), nullable=True)
    nl = Column('Nl', VARCHAR(length=4), nullable=True)
    de = Column('De', VARCHAR(length=4), nullable=True)
    it = Column('It', VARCHAR(length=4), nullable=True)
    pt = Column('Pt', VARCHAR(length=4), nullable=True)
    es = Column('Es', VARCHAR(length=4), nullable=True)
    nL_be = Column('NL_be', VARCHAR(length=4), nullable=True)
    fi = Column('Fi', VARCHAR(length=4), nullable=True)
    da = Column('Da', VARCHAR(length=4), nullable=True)
    pl = Column('pl', VARCHAR(length=4), nullable=True)
    cs = Column('Cs', VARCHAR(length=4), nullable=True)
    el = Column('El', VARCHAR(length=4), nullable=True)
    tr = Column('Tr', VARCHAR(length=4), nullable=True)
    pt_br = Column('Pt_br', VARCHAR(length=4), nullable=True)
    ro = Column('Ro', VARCHAR(length=4), nullable=True)
    hu = Column('Hu', VARCHAR(length=4), nullable=True)
    fr_ch = Column('Fr_ch', VARCHAR(length=4), nullable=True)
    de_ch = Column('De_ch', VARCHAR(length=4), nullable=True)
    sv = Column('Sv', VARCHAR(length=4), nullable=True)
    zh = Column('Zh', VARCHAR(length=4), nullable=True)
    bg = Column('Bg', VARCHAR(length=4), nullable=True)
    ru = Column('Ru', VARCHAR(length=4), nullable=True)
    uk = Column('Uk', VARCHAR(length=4), nullable=True)
    sr = Column('Sr', VARCHAR(length=4), nullable=True)
    ja = Column('Ja', VARCHAR(length=4), nullable=True)
    sq = Column('Sq', VARCHAR(length=4), nullable=True)
    vi = Column('Vi', VARCHAR(length=4), nullable=True)
    fr_ca = Column('Fr_ca', VARCHAR(length=4), nullable=True)
    sk = Column('Sk', VARCHAR(length=4), nullable=True)
    iw = Column('Iw', VARCHAR(length=4), nullable=True)
    ko = Column('ko', VARCHAR(length=4), nullable=True)
    en_ca = Column('En_ca', VARCHAR(length=4), nullable=True)
    zh_tw = Column('Zh_tw', VARCHAR(length=4), nullable=True)
    no = Column('No', VARCHAR(length=4), nullable=True)
    lv = Column('Lv', VARCHAR(length=4), nullable=True)
    et = Column('Et', VARCHAR(length=4), nullable=True)
       
    __tablename__ = 'Lang'
