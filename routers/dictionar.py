from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from dbutils.dbconnect import get_db
import crud.dictionar as cruddict  


router = APIRouter()


@router.get("/api/dict/{tname}/{cname}")
async def read_dict(tname: str, cname: str, db: Session = Depends(get_db)):
    dictionar = cruddict.get_dictionar(db, tname=tname, cname=cname)
    if dictionar is None:
        raise HTTPException(status_code=404, detail="Dictionary row not found")
    return dictionar


@router.get("/api/dict/")
async def list_dict(
        db: Session = Depends(get_db),
        start: int = 0, 
        limit: int = 10,
        cname: str = '',
        tname: str = ''
    ):
    lendicts, dictionars = cruddict.get_dictionars(db=db, skip=start, limit=limit, tname=tname, cname=cname)    
    return {"count": lendicts, "next": start+limit, "items": dictionars}
