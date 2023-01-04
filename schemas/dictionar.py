from typing import Union

from pydantic import BaseModel


class DictionarBase(BaseModel):
    tname: str
    cname: str
    dtype: str
    enable: str

    defaultValue: Union[str, None] = None
    minimum: Union[float, None] = None
    maximum: Union[float, None] = None
    dlist: Union[str, None] = None
    dnatip: Union[int, None] = None
    units: Union[int, None] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class DictionarList(BaseModel):

    count: int    
    items: list[DictionarBase]