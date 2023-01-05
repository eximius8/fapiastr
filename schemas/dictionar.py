from typing import Union

from pydantic import BaseModel


class DictionarBase(BaseModel):
    
    dtype: str
    enable: str

    defaultvalue: Union[str, None] = None
    minimum: Union[float, None] = None
    maximum: Union[float, None] = None
    dlist: Union[str, None] = None
    dnatip: Union[int, None] = None
    zeroallowed: Union[bool, None] = None
    required: Union[bool, None] = None
    anomaly: Union[bool, None] = None
    length: Union[str, None] = None
    global_prop: Union[bool, None] = None
    dna: Union[str, None] = None
    dna_chart: Union[str, None] = None
    minvalue: Union[float, None] = None
    maxvalue: Union[float, None] = None
    special: Union[str, None] = None
    units: Union[int, None] = None

    flagged: Union[bool, None] = None
    dna_flag: Union[int, None] = None
    flag_expression: Union[str, None] = None
    blocks: Union[str, None] = None
    block_multi: Union[bool, None] = None
    flag_link: Union[str, None] = None
    int_precision: Union[int, None] = None
    dec_precision: Union[int, None] = None
    existing_value_changeable: Union[str, None] = None


    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class DictionarSchema(DictionarBase):

    tname: str
    cname: str



class CreateDictionarSchema(DictionarSchema):
    pass


class UpdateDictionarSchema(DictionarBase):
    pass
