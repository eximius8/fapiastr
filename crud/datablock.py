from sqlalchemy.orm import Session

from models.datablock import DataBlock
from models.sequences import Sequence, SequenceData
from schemas.datablock import DatablockCreate, DatablockUpdate



def get_datablock_location_sequences(db: Session, block: int):

    blockobj = db.query(DataBlock).get(block)
    sequences = db.query(SequenceData).filter(SequenceData.block==block)
    if sequences.count() < 1:
        return False
    if sequences.count() == 1:

    


def get_datablock(db: Session, block: int, version: int):
    return db.query(DataBlock).get((block, version))


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

    last_block = db.query(DataBlock).order_by(DataBlock.block.desc()).first().block
    
    db_datablock = DataBlock(**datablock.dict(), block=last_block+1)
    db.add(db_datablock)
    db.commit()
    db.refresh(db_datablock)
    return db_datablock
