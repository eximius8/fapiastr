from dbutils.dbconnect import Base
from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from sqlalchemy.types import VARCHAR, FLOAT, BOOLEAN, SMALLINT
import xml.etree.ElementTree as ET


class Dictionar(Base):
    """Dict model"""
    tname = Column('tname', VARCHAR(length=30), nullable=False)
    cname = Column('cname', VARCHAR(length=30), nullable=False)
    dtype = Column('type', VARCHAR(length=2), nullable=False)

    defaultvalue = Column('defaultvalue', VARCHAR(length=255), nullable=True)
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
    enable = Column('enable', VARCHAR(length=255), nullable=True)
    existing_value_changeable = Column('existing_value_changeable', VARCHAR(length=512), nullable=True)

    __tablename__ = 'dictionary'
    __table_args__ = (
        PrimaryKeyConstraint(tname, cname),        
    )

    def get_xml(self):

        root = ET.Element("row")

        items = [
            {'type': None, 'name': 'TName', 'val': self.tname},
            {'type': None, 'name': 'CName', 'val': self.cname},
            {'type': None, 'name': 'Type', 'val': self.dtype},
            {'type': None, 'name': 'DefaultValue', 'val': self.defaultvalue},
            {'type': None, 'name': 'List', 'val': self.dlist},
            {'type': None, 'name': 'Flag_expression', 'val': self.flag_expression},
            {'type': None, 'name': 'Blocks', 'val': self.blocks},
            {'type': None, 'name': 'Flag_link', 'val': self.flag_link},
    
            {'type': 'N', 'name': 'Minimum', 'val': self.minimum},
            {'type': 'N', 'name': 'Maximum', 'val': self.maximum},
            {'type': 'N', 'name': 'DNA_tip', 'val': self.dnatip},
            {'type': 'B', 'name': 'ZeroAllowed', 'val': self.zeroallowed},
            {'type': 'B', 'name': 'Required', 'val': self.required},
            {'type': 'B', 'name': 'Anomaly', 'val': self.anomaly},
            {'type': 'N', 'name': 'Length', 'val': self.length},
            {'type': 'B', 'name': 'Global', 'val': self.global_prop},
            {'type': 'N', 'name': 'DNA', 'val': self.dna},
            {'type': 'N', 'name': 'DNA_chart', 'val': self.dna_chart},
            {'type': 'N', 'name': 'MinValue', 'val': self.minvalue},
            {'type': 'N', 'name': 'MaxValue', 'val': self.maxvalue},
            {'type': 'N', 'name': 'Special', 'val': self.special},
            {'type': 'N', 'name': 'Units', 'val': self.units},
            {'type': 'B', 'name': 'Flagged', 'val': self.flagged},
            {'type': 'N', 'name': 'DNA_flag', 'val': self.dna_flag},
            {'type': 'B', 'name': 'Block_multi', 'val': self.block_multi},
            {'type': 'N', 'name': 'int_precision', 'val': self.int_precision},
            {'type': 'N', 'name': 'dec_precision', 'val': self.dec_precision}
        ]

        for item in items:
            newsubel = ET.SubElement(root, 'item', name=item['name'])
            if item['val']:
                newsubel.set('val', str(item['val']))
            else:
                newsubel.set('val', 'null')
            if item['type']:
                newsubel.set('type', item['type'])

       

        ET.indent(root)
        return ET.tostring(root).decode('utf-8')
