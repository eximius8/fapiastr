from pydantic import BaseModel, constr
from typing import Optional


class LangSchema(BaseModel):
    """Language model"""
    En: Optional[constr(max_length=2045)] 
    Fr: Optional[constr(max_length=2045)] 
    Nl: Optional[constr(max_length=2045)] 
    De: Optional[constr(max_length=2045)] 
    It: Optional[constr(max_length=2045)] 
    Pt: Optional[constr(max_length=2045)] 
    Es: Optional[constr(max_length=2045)] 
    NL_be: Optional[constr(max_length=2045)] 
    Fi: Optional[constr(max_length=2045)] 
    Da: Optional[constr(max_length=2045)] 
    pl: Optional[constr(max_length=2045)] 
    Cs: Optional[constr(max_length=2045)] 
    El: Optional[constr(max_length=2045)] 
    Tr: Optional[constr(max_length=2045)] 
    Pt_br: Optional[constr(max_length=2045)] 
    Ro: Optional[constr(max_length=2045)] 
    Hu: Optional[constr(max_length=2045)] 
    Fr_ch: Optional[constr(max_length=2045)] 
    De_ch: Optional[constr(max_length=2045)] 
    Sv: Optional[constr(max_length=2045)] 
    Zh: Optional[constr(max_length=2045)] 
    Bg: Optional[constr(max_length=2045)] 
    Ru: Optional[constr(max_length=2045)] 
    Uk: Optional[constr(max_length=2045)] 
    Sr: Optional[constr(max_length=2045)] 
    Ja: Optional[constr(max_length=2045)] 
    Sq: Optional[constr(max_length=2045)] 
    Vi: Optional[constr(max_length=2045)] 
    Fr_ca: Optional[constr(max_length=2045)] 
    Sk: Optional[constr(max_length=2045)] 
    Iw: Optional[constr(max_length=2045)] 
    ko: Optional[constr(max_length=2045)] 
    En_ca: Optional[constr(max_length=2045)] 
    Zh_tw: Optional[constr(max_length=2045)] 
    No: Optional[constr(max_length=2045)] 
    Lv: Optional[constr(max_length=2045)] 
    Et: Optional[constr(max_length=2045)] 

    class Config:
        orm_mode = True

class LangSchemaDNA(LangSchema):

    DNA: Optional[int]
