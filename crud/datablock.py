from sqlalchemy.orm import Session

from models.datablock import DataBlock
from models.sequences import SequenceData
from schemas.datablock import DatablockCreate, DatablockUpdate
from crud.langcrud import get_lang
import re
import uuid



def get_latest_datablock(db: Session, block: int):

    blocks = db.query(DataBlock).filter(DataBlock.block==block)#.order_by(DataBlock.version.desc())
    return blocks.all()[0]


def get_datablock_with_children(db: Session, block: int):

    datablock = get_latest_datablock(db=db, block=block)
    datablockdict = {}
    datablockdict['id'] = uuid.uuid4().hex
    datablockdict['id2'] = datablock.block
    datablockdict['type'] = 'block'
    datablockdict['name'] = f'block {datablock.block}'
    datablockdict['description'] = datablock.description
    if datablock.dna_title: 
        datablockdict['name'] += f': {get_lang(db=db, dna=datablock.dna_title).en}'
    childrenlist = []
    
    allsubblocks = datablock.get_blocks()
    if datablock.details:
        details = re.split('[\s,;]+', datablock.details.strip())
        if details:
            allsubblocks += details
    for subblock in allsubblocks:       
        childrenlist += [get_datablock_with_children(db=db, block=int(subblock))]         
        
    if childrenlist:
        datablockdict['children'] = childrenlist 
    return datablockdict



def get_datablocks_by_sequence(db: Session, sequence: int):

    sequencedatas = db.query(SequenceData).filter(SequenceData.sequence==sequence)
    blocks = []
    for sqdata in sequencedatas.all():
        block = get_datablock_with_children(db=db, block=sqdata.block)
        blocks += [block]
    return blocks



def get_datablock(db: Session, block: int):
    return db.query(DataBlock).get(block)


def get_datablocks(db: Session, skip: int = 0, limit: int = 100, search: str = ""):
    
    if search:
        query = db.query(DataBlock).filter(DataBlock.description.like(f'%{search}%'))
    else:
        query = db.query(DataBlock)
    return query.count(), query.all()[skip:skip+limit]


def update_datablock(db: Session, block: int, version: int, datablock: DatablockUpdate):

    stored_block = db.query(DataBlock).get((block, version))
    update_data = datablock.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(stored_block, key, value)    
    db.commit()
    db.refresh(stored_block)

    return stored_block


def create_datablock(db: Session, datablock: DatablockCreate):

    #last_block = db.query(DataBlock).order_by(DataBlock.block.desc()).first().block
    
    db_datablock = DataBlock(**datablock.dict())
    db.add(db_datablock)
    db.commit()
    db.refresh(db_datablock)
    return db_datablock
