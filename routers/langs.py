from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from dbutils.dbconnect import get_db

from schemas.lang import LangSchema, UpdateLangSchema, CreateLangSchema
import crud.langcrud as crudlang 


router = APIRouter()


@router.get("/api/langs/")
async def list_langs(
        db: Session = Depends(get_db),
        start: int = 0, 
        limit: int = 10,
        search: str = ''
    ):
    next = None
    lenlangs, langs = crudlang.get_langs(db=db, skip=start, limit=limit, search=search) 
    if lenlangs > start+limit:
        next = start+limit
    return {"count": lenlangs, "next": next, "items": langs}


@router.get("/api/langs/{dna}")
async def read_lang(dna: int, db: Session = Depends(get_db)):
    lang_object = crudlang.get_lang(db, dna=dna)
    if lang_object is None:
        raise HTTPException(status_code=404, detail="Lang object not found")
    return lang_object


@router.delete("/api/langs/{dna}", status_code=204)
async def delete_lang(dna: int, db: Session = Depends(get_db)):
    
    if crudlang.delete_lang(db, dna=dna):
        return {'status': 'deleted'}
        
    raise HTTPException(status_code=404, detail="Lang row not found")


@router.post("/api/langs/", status_code=201, response_model=LangSchema)
async def create_lang(langdata: CreateLangSchema, db: Session = Depends(get_db)):

    new_itm = crudlang.create_lang(db, langweb=langdata)
    if new_itm:
        return new_itm
    raise HTTPException(status_code=400, detail="Error occurred") 


@router.patch("/api/langs/{dna}", response_model=LangSchema)
async def update_lang(dna: int, langweb: UpdateLangSchema, db: Session = Depends(get_db)):

    updated_lang = crudlang.update_lang(db=db, dna=dna, langweb=langweb)
    if updated_lang is None:
        raise HTTPException(status_code=404, detail="Lang row not found")
    return updated_lang
