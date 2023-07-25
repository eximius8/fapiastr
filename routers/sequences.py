from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from dbutils.dbconnect import get_db

from crud.sequences import get_root_sequences 



router = APIRouter()


@router.get("/api/datastructure/")
async def read_sequences(db: Session = Depends(get_db)):
    
    sequences = get_root_sequences(db=db, parent=0)
    
    return sequences