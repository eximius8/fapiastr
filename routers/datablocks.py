from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union

from schemas.datablock import Datablock, DatablockXML, DatablockCreate, DatablockUpdate, DataBlockList
import crud.datablock as cruddatablock
from dbutils.dbconnect import get_db

#from models.datablock import DataBlock
#from fastapi import APIRouter
#from dbutils.dbconnect import loadSession, engine
#import xmltodict



router = APIRouter()


@router.get("/api/datablock/xml/{block}/{version}")
def read_datablockxml(block: int, version: int, db: Session = Depends(get_db)):
    datablock = cruddatablock.get_datablock(db, block=block, version=version)
    if datablock is None:
        raise HTTPException(status_code=404, detail="datablock not found")
    return datablock


@router.get("/api/datablock/{block}", response_model=Datablock)
def read_datablock(block: int, db: Session = Depends(get_db)):
    datablock = cruddatablock.get_datablock(db, block=block)
    if datablock is None:
        raise HTTPException(status_code=404, detail="datablock not found")
    return datablock


@router.get("/api/datablock/", response_model=DataBlockList)
def read_datablocks(
        db: Session = Depends(get_db), 
        search: Union[str, None] = None,
        start: int = 0, 
        limit: int = 15):
    count, datablocks = cruddatablock.get_datablocks(db=db, skip=start, limit=limit, search=search)
  
    return {"count": count, "items": datablocks}
    

@router.post("/api/datablock/", response_model=Datablock)
def create_datablock(datablock: DatablockCreate, db: Session = Depends(get_db)):   

    return cruddatablock.create_datablock(db=db, datablock=datablock)


@router.patch("/api/datablock/{block}/{version}", response_model=Datablock)
async def update_datablock(block: int, version: int, datablock: DatablockUpdate, db: Session = Depends(get_db)):

    return cruddatablock.update_datablock(db=db, version=version, block=block, datablock=datablock)




#@router.get("/api/datablock/")
#async def list_datablocks(
#        start: int = 0, 
#        limit: int = 10, 
#    ):
#    session = loadSession()
#    datablocks = session.query(DataBlock)   
#    datablocks = datablocks.all()
#    lengt = len(datablocks)
#    datablocks = datablocks[start:start+limit]
#    session.close()
#    return {"count": lengt, "next": start+limit, "items": datablocks}
#
#
#@router.get("/api/datablock/{block}-{version}")
#async def read_block(
#        block: int,
#        version: int
#    ):
#
#    session = loadSession()
#    datablock = session.query(DataBlock).get((block, version))
#    if datablock is None:
#        return {'error': 'Does not exist'}
#    session.close()
#    dict_data = xmltodict.parse(datablock.contents) 
#    return datablock
#    return {'main': datablock, 'contents': dict_data['block']['item']}
#