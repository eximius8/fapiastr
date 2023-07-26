from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from dbutils.dbconnect import get_db

from crud.sequences import get_root_sequences 



router = APIRouter()

def sortedDeep(d):
    if isinstance(d,list):
        return sorted([sortedDeep(v) for v in d], key=lambda d: d['id2'] + (d['type'] == 'block')*10000)
    if isinstance(d, dict):
        if 'children' in d:
            newd = d
            newd['children'] = sortedDeep(d['children'])
            return newd
            # return {**d, 'children': sortedDeep(d['children'])}
        return d
    return d


@router.get("/api/datastructure/")
async def read_sequences(db: Session = Depends(get_db)):
    
    sequences = get_root_sequences(db=db, parent=0)
    
    return sortedDeep(sequences)  #sorted(sequences, key=lambda d: d['id2'])