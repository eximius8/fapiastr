from sqlalchemy.orm import Session


from models.sequences import Sequence

from crud.langcrud import get_lang
from crud.datablock import get_datablocks_by_sequence


def get_root_sequences(db: Session, parent):
    """RECURSIVE!"""

    seqns = db.query(Sequence).filter(Sequence.parent==parent, Sequence.setname=='Full')
    if seqns.count() < 1:
        return
    seqlist = []
    seqdict = {}
    for sqen in seqns.all():
        seqdict['id'] = sqen.id
        seqdict['dna'] = get_lang(db=db, dna=sqen.dna).en
        seqdict['children'] = get_root_sequences(db=db, parent=sqen.id)
        seqdict['blocks'] = get_datablocks_by_sequence(db=db, sequence=sqen.id)
        seqlist += [{**seqdict}]
    return seqlist