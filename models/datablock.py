from dbutils.dbconnect import Base
from typing import List
from pydantic_xml import BaseXmlModel, attr, element
from sqlalchemy import Column, Integer, SmallInteger, LargeBinary, PrimaryKeyConstraint
from sqlalchemy.types import VARCHAR, DATETIME
import xml.etree.ElementTree as ET

from schemas.datablockcommon import ItemCommon

class Item(ItemCommon):    
    pk: str = attr(name='id', max_length=4, regex=r'^[1-9](\d+)?$')
    
    

class Block(BaseXmlModel, tag='block'):
    items: List[Item] = element(tag='item')


class DataBlock(Base):
    """Language model"""
    block = Column('block', Integer, nullable=False)
    version = Column('version', SmallInteger, nullable=False)

    tabtable = Column('tabtable', VARCHAR(length=31), nullable=True)
    dnatitle = Column('dna_title', Integer, nullable=True)
    tabname = Column('tabname', Integer, nullable=True)
    tabnew = Column('tabnew', Integer, nullable=True)
    details = Column('details', VARCHAR(length=255), nullable=True)
    description = Column('description', VARCHAR(length=255), nullable=True) 
    dnainfo = Column('dna_info', Integer, nullable=True)
    _contents = Column('contents', LargeBinary, nullable=True)   
    typename = Column('typename', VARCHAR(length=255), nullable=True)
    
    layout = Column('layout', SmallInteger, nullable=True)
    sset = Column('sset', VARCHAR(length=3), nullable=True)
    helpid = Column('helpid', VARCHAR(length=40), nullable=True)
    tag = Column('tag', VARCHAR(length=10), nullable=True)

    created_at = Column('created_at', DATETIME, nullable=True)
    creator = Column('creator', VARCHAR(length=20), nullable=True)
    issue = Column('issue', VARCHAR(length=20), nullable=True)
    dnaprint = Column('dna_print', Integer, nullable=True)


    @property
    def contents(self):
        block = Block.from_xml(self._contents.decode('utf-8'))
        return block
    
    @contents.setter
    def contents(self, value):
        contents = Block.parse_obj(value)    
        self._contents = contents.to_xml(skip_empty=True)


    __tablename__ = 'DataBlock'
    __table_args__ = (
        PrimaryKeyConstraint(block, version),        
    )

#    def findUnits(self):        
#        dnas = {}
#        dnasinit = {
#                'block': self.block, 
#                'v': self.version,
#                'blocktitle': self.dnatitle,
#                'blockdesc': self.dnainfo
#            }
#        searchstr = self.contents.decode('utf-8')
#        root = ET.fromstring(searchstr)       
#            
#        
#    
#    
#    def findDNA(self, dna):        
#        dnas = {}
#        dnasinit = {
#                'block': self.block, 
#                'v': self.version,
#                'blocktitle': self.dnatitle,
#                'blockdesc': self.dnainfo
#            }
#        searchstr = self.contents.decode('utf-8')
#        root = ET.fromstring(searchstr)
#        
#            
#        for child in root:
#            if 'dna' in child.keys():                
#                if str(dna) == child.get('dna'):                    
#                    dnas[f'item{child.get("id")}'] = child.get("id")
#        if self.dnatitle == dna or self.dnainfo == dna or self.dnaprint == dna or dnas:
#            return {**dnasinit, **dnas}
#        
        

    __tablename__ = 'DataBlock'
    __table_args__ = (
        PrimaryKeyConstraint(block, version),        
    )