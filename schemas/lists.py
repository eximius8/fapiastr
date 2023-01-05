from typing import Union
from pydantic import BaseModel


class ListBase(BaseModel):    

    defaultitem: Union[bool, None] = None
    alert: Union[bool, None] = None
    dna: Union[int, None] = None
    lorder: Union[int, None] = None
    child: Union[str, None] = None
    deleted: Union[bool, None] = None
    associated: Union[str, None] = None
    department: Union[str, None] = None
    tag: Union[str, None] = None
    issue: Union[str, None] = None
    parenttext: Union[bool, None] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ListSchema(ListBase):

    id: int
    listname: str
    version: int


class CreateListSchema(ListSchema):
    pass


class UpdateListSchema(ListBase):
    pass
