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

    _contents = Column('contents', LargeBinary, nullable=True)   
    created_at = Column('created_at', DATETIME, nullable=True)
    creator = Column('creator', VARCHAR(length=20), nullable=True)
    description = Column('description', VARCHAR(length=255), nullable=True) 
    details = Column('details', VARCHAR(length=255), nullable=True)
    dna_info = Column('dna_info', Integer, nullable=True)
    dna_print = Column('dna_print', Integer, nullable=True)
    dna_title = Column('dna_title', Integer, nullable=True)
    helpid = Column('helpid', VARCHAR(length=40), nullable=True)
    issue = Column('issue', VARCHAR(length=20), nullable=True)
    layout = Column('layout', SmallInteger, nullable=True)
    sset = Column('sset', VARCHAR(length=3), nullable=True)
    tabname = Column('tabname', Integer, nullable=True)
    tabnew = Column('tabnew', Integer, nullable=True)
    tabtable = Column('tabtable', VARCHAR(length=31), nullable=True)
    tag = Column('tag', VARCHAR(length=10), nullable=True)
    typename = Column('typename', VARCHAR(length=255), nullable=True)

    def get_xml(self):        

        root = ET.Element("root")
        block = ET.fromstring(self._contents.decode('utf-8'))
        root.insert(0, block)
        blocknum = ET.SubElement(root, "number").text = str(self.block)
        blockversion = ET.SubElement(root, "version").text = str(self.version)
        if self.created_at:
            ET.SubElement(root, "createdat").text = str(self.created_at.strftime("%d.%m.%Y"))
        if self.creator:
            ET.SubElement(root, "creator").text = str(self.creator)
        if self.description:
            ET.SubElement(root, "description").text = str(self.description)
        if self.details:
            ET.SubElement(root, "details").text = str(self.details)
        if self.dna_info:
            ET.SubElement(root, "dnainfo").text = str(self.dna_info)
        if self.dna_print:
            ET.SubElement(root, "dnaprint").text = str(self.dna_print)
        if self.dna_title:
            ET.SubElement(root, "dnatitle").text = str(self.dna_title)
        if self.helpid:
            ET.SubElement(root, "helpid").text = str(self.helpid)
        if self.issue:
            ET.SubElement(root, "issue").text = str(self.issue)
        if self.layout:
            ET.SubElement(root, "layout").text = str(self.layout)
        if self.sset:
            ET.SubElement(root, "sset").text = str(self.sset)
        if self.tabname:
            ET.SubElement(root, "tabname").text = str(self.tabname)
        if self.tabnew:
            ET.SubElement(root, "tabnew").text = str(self.tabnew)
        if self.tabtable:
            ET.SubElement(root, "tabtable").text = str(self.tabtable)
        if self.tag:
            ET.SubElement(root, "tag").text = str(self.tag)
        if self.typename:
            ET.SubElement(root, "typename").text = str(self.typename)
        ET.indent(root)
        return ET.tostring(root)

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