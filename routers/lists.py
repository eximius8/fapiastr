from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from dbutils.dbconnect import get_db
import crud.lists as crudlist
from schemas.lists import ListBase


router = APIRouter()


@router.get("/api/lists/{id}/{listname}/{version}")
async def read_dict(id: int, listname: str, version: int, db: Session = Depends(get_db)):
    list_object = crudlist.get_list(db, id=id, listname=listname, version=version)
    if list_object is None:
        raise HTTPException(status_code=404, detail="List object not found")
    return list_object