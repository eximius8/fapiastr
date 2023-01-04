from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from dbutils.dbconnect import get_db
import crud.lists as crudlist
from schemas.lists import ListObject, CreateListObject, UpdateListObject


router = APIRouter()


@router.get("/api/lists/{id}/{listname}/{version}", response_model=ListObject)
async def read_list(id: int, listname: str, version: int, db: Session = Depends(get_db)):
    list_object = crudlist.get_list(db, id=id, listname=listname, version=version)
    if list_object is None:
        raise HTTPException(status_code=404, detail="List object not found")
    return list_object


@router.get("/api/lists/")
async def list_lists(
        db: Session = Depends(get_db),
        start: int = 0, 
        limit: int = 10,
        listname: str = ''
    ):
    next = None
    lenlists, lists = crudlist.get_lists(db=db, skip=start, limit=limit, listname=listname) 
    if lenlists > start+limit:
        next = start+limit
    return {"count": lenlists, "next": next, "items": lists}


@router.delete("/api/lists/{id}/{listname}/{version}", status_code=204)
async def delete_list(id: int, listname: str, version: int, db: Session = Depends(get_db)):
    
    if crudlist.delete_list(db, id=id, listname=listname, version=version):
        return {'status': 'deleted'}
        
    raise HTTPException(status_code=404, detail="List row not found")


@router.post("/api/list/", status_code=201, response_model=ListObject)
async def create_list(listdata: CreateListObject, db: Session = Depends(get_db)):

    new_itm = crudlist.create_list(db, listweb=listdata)
    if new_itm:
        return new_itm
    raise HTTPException(status_code=400, detail="Error occurred") 


@router.patch("/api/list/{id}/{listname}/{version}", response_model=ListObject)
async def update_list(id: int, listname: str, version: int, listweb: UpdateListObject, db: Session = Depends(get_db)):

    updated_list = crudlist.update_list(db=db, id=id, listname=listname, version=version, listweb=listweb)
    if updated_list is None:
        raise HTTPException(status_code=404, detail="List row not found")
    return updated_list
