from typing import Union, List

from pydantic import BaseModel
from pydantic_xml import BaseXmlModel, attr, element

from schemas.datablockcommon import ItemCommon, ItemCommonAll


class ItemAll(ItemCommonAll):

    #pk: str = attr(name='id', max_length=4, regex=r'^[1-9](\d+)?$')

    def dict(self, *args, **kwargs):
        
        kwargs["exclude_none"] = True
        return BaseXmlModel.dict(self, *args, **kwargs)



# Specific itmes only 
class Item(ItemCommon):    
   # pk: str = attr(name='id', max_length=4, regex=r'^[1-9](\d+)?$')
    
    def dict(self, *args, **kwargs):
        
        kwargs["exclude_none"] = True
        return BaseXmlModel.dict(self, *args, **kwargs)
    

class Block(BaseXmlModel, tag='block'):
    items: List[Item] = element(tag='item')


class DatablockBase(BaseModel):
    dna_title: Union[int, None] = None
    dna_info: Union[int, None] = None
    description: Union[str, None] = None
    typename: Union[str, None] = None
    details: Union[str, None] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class DataBlockBaseID(DatablockBase):
    block: int
    version: int


class DataBlockList(BaseModel):

    count: int
    
    items: list[DataBlockBaseID]


class DatablockCreate(DatablockBase):
    contents: Block


class DatablockUpdate(DatablockBase):
    contents: Union[Block, None] = None


class Datablock(DatablockBase):
    block: int
    
    contents: Block 

    class Config:
        orm_mode = True


class DatablockXML(BaseModel):

    class Config:
        orm_mode = True
