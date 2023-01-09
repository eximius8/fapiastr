from sqlalchemy.orm import Session

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

    new_lang = LangObject(**langweb.dict(exclude_unset=True))
    db.add(new_lang)
    db.commit()
    db.refresh(new_lang)
    return new_lang


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
