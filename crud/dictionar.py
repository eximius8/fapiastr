from sqlalchemy.orm import Session

from schemas.dictionar import DictionarBase
from models.dictionar import Dictionar


def get_dictionar(db: Session, tname: str, cname: str):

    return db.query(Dictionar).get((tname, cname))


def get_dictionars(db: Session, skip: int = 0, limit: int = 100, cname: str = "", tname: str = "",):

    query = db.query(Dictionar)
    if cname:
        query = query.filter(Dictionar.cname.like(f'%{cname}%'))
    if tname:
        query = query.filter(Dictionar.tname.like(f'%{tname}%'))    
    return query.count(), query.all()[skip:skip+limit]
    

def update_dictionar(db: Session, tname: str, cname: str, dictionarweb: DictionarBase):

    stored_dictionar = db.query(Dictionar).get((tname, cname))
    if not stored_dictionar:
        return None
    update_data = dictionarweb.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(stored_dictionar, key, value)    
    db.commit()
    db.refresh(stored_dictionar)

    return stored_dictionar


def delete_dictionar(db: Session, tname: str, cname: str):

    deleted_dict = db.query(Dictionar).get((tname, cname))
    if deleted_dict:
        db.delete(deleted_dict)
        db.commit()
        return True


def create_dictionar(db: Session, dictionarweb: DictionarBase):

    newdictdata = dictionarweb.dict(exclude_unset=True)
    if db.query(Dictionar).get((newdictdata['tname'], newdictdata['cname'])):
        return False

    new_dictionar = Dictionar(**dictionarweb.dict(exclude_unset=True))
    db.add(new_dictionar)
    db.commit()
    db.refresh(new_dictionar)
    return new_dictionar
