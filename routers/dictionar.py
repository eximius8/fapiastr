from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from dbutils.dbconnect import get_db
import crud.dictionar as cruddict
from schemas.dictionar import DictionarBase


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
    next = None
    lendicts, dictionars = cruddict.get_dictionars(db=db, skip=start, limit=limit, tname=tname, cname=cname) 
    if lendicts > start+limit:
        next = start+limit
    return {"count": lendicts, "next": next, "items": dictionars}


@router.patch("/api/dict/{tname}/{cname}", response_model=DictionarBase)
async def update_dictionar(tname: str, cname: str, dictionar: DictionarBase, db: Session = Depends(get_db)):

    updated_dict = cruddict.update_dictionar(db=db, cname=cname, tname=tname, dictionarweb=dictionar)
    if updated_dict is None:
        raise HTTPException(status_code=404, detail="Dictionary row not found")
    return updated_dict


@router.delete("/api/dict/{tname}/{cname}", status_code=204)
async def delete_dictionar(tname: str, cname: str, db: Session = Depends(get_db)):
    
    if cruddict.delete_dictionar(db, tname=tname, cname=cname):
        return {'status': 'deleted'}
        
    raise HTTPException(status_code=404, detail="Dictionary row not found")


@router.post("/api/dict/", status_code=201)
async def create_dictionar(dictionar: DictionarBase, db: Session = Depends(get_db)):

    new_itm = cruddict.create_dictionar(db, dictionarweb=dictionar)
    if new_itm:
        return new_itm
    raise HTTPException(status_code=400, detail="Error occurred") 
