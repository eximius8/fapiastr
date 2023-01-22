from pydantic import BaseModel, constr
from typing import Optional


class LangBase(BaseModel):
    """Language model"""
    en: Optional[constr(max_length=2045)] 
    fr: Optional[constr(max_length=2045)] 
    nl: Optional[constr(max_length=2045)] 
    de: Optional[constr(max_length=2045)] 
    it: Optional[constr(max_length=2045)] 
    pt: Optional[constr(max_length=2045)] 
    es: Optional[constr(max_length=2045)] 
    nL_be: Optional[constr(max_length=2045)] 
    fi: Optional[constr(max_length=2045)] 
    da: Optional[constr(max_length=2045)] 
    pl: Optional[constr(max_length=2045)] 
    cs: Optional[constr(max_length=2045)] 
    el: Optional[constr(max_length=2045)] 
    tr: Optional[constr(max_length=2045)] 
    pt_br: Optional[constr(max_length=2045)] 
    ro: Optional[constr(max_length=2045)] 
    hu: Optional[constr(max_length=2045)] 
    fr_ch: Optional[constr(max_length=2045)] 
    de_ch: Optional[constr(max_length=2045)] 
    sv: Optional[constr(max_length=2045)] 
    zh: Optional[constr(max_length=2045)] 
    bg: Optional[constr(max_length=2045)] 
    ru: Optional[constr(max_length=2045)] 
    uk: Optional[constr(max_length=2045)] 
    sr: Optional[constr(max_length=2045)] 
    ja: Optional[constr(max_length=2045)] 
    sq: Optional[constr(max_length=2045)] 
    vi: Optional[constr(max_length=2045)] 
    fr_ca: Optional[constr(max_length=2045)] 
    sk: Optional[constr(max_length=2045)] 
    iw: Optional[constr(max_length=2045)] 
    ko: Optional[constr(max_length=2045)] 
    en_ca: Optional[constr(max_length=2045)] 
    zh_tw: Optional[constr(max_length=2045)] 
    no: Optional[constr(max_length=2045)] 
    lv: Optional[constr(max_length=2045)] 
    et: Optional[constr(max_length=2045)] 

    class Config:
        orm_mode = True


class LangSchema(LangBase):

    dna: int


class CreateLangSchema(LangBase):
    pass


class UpdateLangSchema(LangBase):
    pass
