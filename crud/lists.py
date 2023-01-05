from sqlalchemy.orm import Session

from schemas.lists import CreateListSchema, UpdateListSchema
from models.lists import Listobject


def get_list(db: Session, id: int, listname: str, version: int):

    return db.query(Listobject).get((id, listname, version))


def get_lists(db: Session, skip: int = 0, limit: int = 10, listname: str = ""):

    query = db.query(Listobject)
    if listname:
        query = query.filter(Listobject.listname.like(f'%{listname}%'))
    
    return query.count(), query.all()[skip:skip+limit]


def delete_list(db: Session, id: int, listname: str, version: int):

    deleted_list = db.query(Listobject).get((id, listname, version))
    if deleted_list:
        db.delete(deleted_list)
        db.commit()
        return True


def create_list(db: Session, listweb: CreateListSchema):

    newlistdata = listweb.dict(exclude_unset=True)
    if db.query(Listobject).get((newlistdata['id'], newlistdata['listname'], newlistdata['version'])):
        return False

    new_list = Listobject(**listweb.dict(exclude_unset=True))
    db.add(new_list)
    db.commit()
    db.refresh(new_list)
    return new_list


def update_list(db: Session, id: int, listname: str, version: str, listweb: UpdateListSchema):

    stored_list = db.query(Listobject).get((id, listname, version))
    if not stored_list:
        return None
    update_data = listweb.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(stored_list, key, value)    
    db.commit()
    db.refresh(stored_list)

    return stored_list
