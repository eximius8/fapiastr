from schemas.lang import LangSchema, LangSchemaDNA
from models.lang import Lang
from models.datablock import DataBlock
from fastapi import APIRouter
from dbutils.dbconnect import loadSession, engine
from sqlalchemy.sql import text

router = APIRouter()


@router.get("/api/lang/")
async def list_lang(
        start: int = 0, 
        limit: int = 10, 
        en: str = "", 
        de: str = "", 
        it: str = "", 
        es: str = "", 
        ru: str = "",
    ):
    session = loadSession()
    langs = session.query(Lang)
    if en:
        langs = langs.filter(Lang.En.like(f'%{en}%'))
    if de:
        langs = langs.filter(Lang.De.like(f'%{de}%'))
    if es:
        langs = langs.filter(Lang.Es.like(f'%{es}%'))
    if it:
        langs = langs.filter(Lang.It.like(f'%{it}%'))
    if ru:
        langs = langs.filter(Lang.Ru.like(f'%{ru}%'))
    langs = langs.order_by(Lang.DNA).all()
    lengt = len(langs)
    langs = langs[start:start+limit]
    session.close()
    return {"count": lengt, "next": start+limit, "items": langs}


@router.get("/api/lang/{dna}")
async def read_lang(dna: int):

    session = loadSession()
    lang = session.query(Lang).get(dna)
    if lang is None:
        return {'error': 'Does not exist'}
    d = {}
    for column in lang.__table__.columns:
        d[column.name] = str(getattr(lang, column.name))
    session.close()
    return  d

@router.get("/api/lang/{dna}/usage")
async def read_lang(dna: int):

    session = loadSession()
    lang = session.query(Lang).get(dna)
    if lang is None:
        return {'error': 'Does not exist'}
    dblocks = session.query(DataBlock).all()
    d = []
    for dblock in dblocks:
        data = dblock.findDNA(dna)
        if data:
            d += [data]
    session.close()
    return  d

@router.post("/api/lang/", response_model=LangSchemaDNA)
async def update_lang(langdata: LangSchema):    
   
    seializedlang = langdata.dict(exclude_unset=True)
    session = loadSession()
    obj = session.query(Lang).order_by(Lang.DNA.desc()).all()[0:1] 
    newDNA = obj[0].DNA + 1
    d = {'DNA': newDNA}
    rawsql1 = f"INSERT INTO Lang (DNA"
    rawsql2 = f" VALUES ({newDNA}"    

    for key, value in seializedlang.items():
        rawsql1 += f",{key}"
        rawsql2 += f",'{value}'"
        d[key] = value 
    rawsql = rawsql1 + ') ' + rawsql2 + ');'
    with engine.connect() as con:
        statement = text(rawsql)
        con.execute(statement)

    session.commit()
    session.close()    
    return d


@router.patch("/api/lang/{dna}", response_model=LangSchema)
async def update_lang(dna: int, langdata: LangSchema):    
   
    seializedlang = langdata.dict(exclude_unset=True)

    session = loadSession()   
    langdata = session.query(Lang).get(dna)

    for key, value in seializedlang.items():
        setattr(langdata, key, value) 
    
    d = {}
    for column in langdata.__table__.columns:
        d[column.name] = str(getattr(langdata, column.name))

    session.commit()
    session.close()
    return d
