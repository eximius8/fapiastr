from sqlalchemy.orm import Session

from models.dictionar import Dictionar



def get_dictionar(db: Session, tname: str, cname: str):

    return db.query(Dictionar).get((tname, cname))


def get_dictionars(db: Session, skip: int = 0, limit: int = 100, cname: str = "", tname: str = "",):

    query = db.query(Dictionar)
    if cname:
        query = query.filter(Dictionar.cname.like(f'%{cname}%'))
    if tname:
        query = query.filter(Dictionar.tname.like(f'%{tname}%'))
    
    return query.count(), query.all()[skip:skip+limit]
    

#
#def update_datablock(db: Session, block: int, datablock: DatablockUpdate):
#
#    stored_block = db.query(DataBlock).filter(DataBlock.block == block).first()
#    update_data = datablock.dict(exclude_unset=True)
#    for key, value in update_data.items():
#        setattr(stored_block, key, value)    
#    db.commit()
#    db.refresh(stored_block)
#
#    return stored_block
#
#def create_datablock(db: Session, datablock: DatablockCreate):
#
#    last_block = db.query(DataBlock).order_by(DataBlock.block.desc()).first().block
#    
#    db_datablock = DataBlock(**datablock.dict(), block=last_block+1)
#    db.add(db_datablock)
#    db.commit()
#    db.refresh(db_datablock)
#    return db_datablock
#