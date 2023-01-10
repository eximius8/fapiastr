from sqlalchemy.orm import Session
from sqlalchemy import text

from schemas.lang import CreateLangSchema, UpdateLangSchema
from models.lang import LangObject


def get_lang(db: Session, dna: int):
    """Get single lang object"""
    return db.query(LangObject).get(dna)


def get_langs(db: Session, skip: int = 0, limit: int = 100, search: str = ""):
    """Get multiple lang objects"""

    query = db.query(LangObject)
    if search:
        query = query.filter(LangObject.En.like(f'%{search}%'))
    
    return query.count(), query.all()[skip:skip+limit]


def delete_lang(db: Session, dna: int):
    """Delete lang item"""

    deleted_lang = db.query(LangObject).get(dna)
    if deleted_lang:
        db.delete(deleted_lang)
        db.commit()
        return True
    

def create_lang(db: Session, langweb: CreateLangSchema):
    """Create lang item"""

    # get last lang DNA
    seializedlang = langweb.dict(exclude_unset=True)
    last_obj = db.query(LangObject).order_by(LangObject.DNA.desc()).all()[0:1]
    newDNA = last_obj[0].DNA + 1

    d = {'DNA': newDNA}
    rawsql1 = f"INSERT INTO Lang (DNA"
    rawsql2 = f" VALUES ({newDNA}"    

    for key, value in seializedlang.items():
        rawsql1 += f",{key}"
        rawsql2 += f",'{value}'"
        d[key] = value 
    rawsql = rawsql1 + ') ' + rawsql2 + ');'
    statement = text(rawsql)
    engine = db.get_bind()
    engine.execute(statement)
    return db.query(LangObject).get(newDNA)


def update_lang(db: Session,  dna: int, langweb: UpdateLangSchema):
    """Update lang item"""

    stored_lang = db.query(LangObject).get(dna)
    if not stored_lang:
        return None
    update_data = langweb.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(stored_lang, key, value)    
    db.commit()
    db.refresh(stored_lang)

    return stored_lang
