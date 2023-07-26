from sqlalchemy.orm import Session
import uuid

from models.sequences import Sequence

from crud.langcrud import get_lang
from crud.datablock import get_datablocks_by_sequence


def get_root_sequences(db: Session, parent: int):
    """RECURSIVE!"""
    
    seqns = db.query(Sequence).filter(Sequence.parent==parent, Sequence.setname=='Full')
    if seqns.count() < 1:
        return []
    seqlist = []
    seqdict = {}
    for sqen in seqns.all():
        seqdict['id'] = uuid.uuid4().hex
        seqdict['id2'] = sqen.id

        seqdict['name'] = get_lang(db=db, dna=sqen.dna).en
        seqdict['type'] = 'sequence'
        seqdict['license'] = sqen.licensed
        seqdict['sset'] = sqen.sset
        seqdict['control'] = sqen.control
        seqdict['children'] = get_root_sequences(db=db, parent=sqen.id) + get_datablocks_by_sequence(db=db, sequence=sqen.id)
        seqlist += [{**seqdict}]
    return seqlist