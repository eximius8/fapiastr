from dbutils.dbconnect import Base
from sqlalchemy import Column, Integer, SmallInteger, LargeBinary, PrimaryKeyConstraint
from sqlalchemy.types import VARCHAR
import xml.etree.ElementTree as ET


class DataBlock(Base):
    """Language model"""
    block = Column('block', Integer, nullable=False)
    tabtable = Column('tabtable', VARCHAR(length=31), nullable=True)
    dnatitle = Column('dna_title', Integer, nullable=True)
    tabname = Column('tabname', Integer, nullable=True)
    tabnew = Column('tabnew', Integer, nullable=True)
    details = Column('details', VARCHAR(length=255), nullable=True)
    description = Column('description', VARCHAR(length=255), nullable=True) 
    dnainfo = Column('dna_info', Integer, nullable=True)
    contents = Column('contents', LargeBinary, nullable=True)   
    version = Column('version', SmallInteger, nullable=False)
    typename = Column('typename', VARCHAR(length=255), nullable=True)
    dnaprint = Column('dna_print', Integer, nullable=True)

    def findUnits(self):        
        dnas = {}
        dnasinit = {
                'block': self.block, 
                'v': self.version,
                'blocktitle': self.dnatitle,
                'blockdesc': self.dnainfo
            }
        searchstr = self.contents.decode('utf-8')
        root = ET.fromstring(searchstr)       
            
        
    
    
    def findDNA(self, dna):        
        dnas = {}
        dnasinit = {
                'block': self.block, 
                'v': self.version,
                'blocktitle': self.dnatitle,
                'blockdesc': self.dnainfo
            }
        searchstr = self.contents.decode('utf-8')
        root = ET.fromstring(searchstr)
        
            
        for child in root:
            if 'dna' in child.keys():                
                if str(dna) == child.get('dna'):                    
                    dnas[f'item{child.get("id")}'] = child.get("id")
        if self.dnatitle == dna or self.dnainfo == dna or self.dnaprint == dna or dnas:
            return {**dnasinit, **dnas}
        
        

    __tablename__ = 'DataBlock'
    __table_args__ = (
        PrimaryKeyConstraint(block, version),        
    )