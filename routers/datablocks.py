from models.datablock import DataBlock
from fastapi import APIRouter
from dbutils.dbconnect import loadSession, engine


router = APIRouter()


@router.get("/api/datablock/")
async def list_datablocks(
        start: int = 0, 
        limit: int = 10, 
    ):
    session = loadSession()
    datablocks = session.query(DataBlock)   
    datablocks = datablocks.all()
    lengt = len(datablocks)
    datablocks = datablocks[start:start+limit]
    session.close()
    return {"count": lengt, "next": start+limit, "items": datablocks}


@router.get("/api/datablock/{block}-{version}")
async def read_lang(
        block: int,
        version: int
    ):

    session = loadSession()
    datablock = session.query(DataBlock).get((block, version))
    if datablock is None:
        return {'error': 'Does not exist'}
    session.close()
    print(datablock)
    return  datablock