from pydantic_xml import BaseXmlModel, attr
from typing import Optional, Literal, Dict


class ItemCommonAll(BaseXmlModel):

    __root__: Dict[str, str]


class ItemCommon(BaseXmlModel):

    assoc_enable: Optional[str] = attr(name='assoc_enable')
    link: Optional[str] = attr(name='link')
    ltype: Optional[str] = attr(name='ltype')
    printif: Optional[str] = attr(name='printif')

    item_type: Literal['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z'] = attr(name='type')
    tname: Optional[str] = attr(name='tname')
    cname: Optional[str] = attr(name='cname')

    dec_precision: Optional[str] = attr(name='dec_precision')
    int_precision: Optional[str] = attr(name='int_precision')

    groupdef: Optional[str] = attr(name='groupdef')
    groupbutton: Optional[str] = attr(name='groupbutton')
    future: Optional[str] = attr(name='future')
    definition: Optional[str] = attr(name='definition')
    configuration: Optional[str] = attr(name='configuration')
    condition: Optional[str] = attr(name='condition')
    chart: Optional[str] = attr(name='chart')
    assoc: Optional[str] = attr(name='assoc')


    col: Optional[str] = attr(name='col', max_length=10, regex=r'^(0|[1-9](\d+)?)$')
    dna: Optional[str] = attr(name='dna', max_length=10, regex=r'^(0|[1-9](\d+)?)$')
    width: Optional[str] = attr(name='width', max_length=4, regex=r'^(0|[1-9](\d+)?)$')
    nrows: Optional[str] = attr(name='nrows', max_length=4, regex=r'^(0|[1-9](\d+)?)$') # , regex=r'^[1-9](\d+)?$'
    printhint: Optional[str] = attr(name='printhint', max_length=10, regex=r'^(0|[1-9](\d+)?)$')
    printdna: Optional[str] = attr(name='printdna', max_length=10, regex=r'^(0|[1-9](\d+)?)$')
    layout: Optional[str] = attr(name='layout', regex=r'^(0|[1-9](\d+)?)$')
    subblock: Optional[str] = attr(name='subblock', max_length=4, regex=r'^(0|[1-9](\d+)?)$')
    target: Optional[str] = attr(name='target', max_length=1, regex=r'^[0-3]$')
    textstyle: Optional[str] = attr(name='textstyle')
    calc: Optional[str] = attr(name='calc') 
    precision: Optional[str] = attr(name='precision')
    popupid: Optional[str] = attr(name='popupid')
    pdef: Optional[str] = attr(name='pdef')
    nospell: Optional[str] = attr(name='nospell')
    nexttab: Optional[str] = attr(name='nexttab')
    pcheckbox: Optional[str] = attr(name='pcheckbox')
    name: Optional[str] = attr(name='name')
    list_item: Optional[str] = attr(name='list')
    locked: Optional[str] = attr(name='locked')
    labelcomponent: Optional[str] = attr(name='labelcomponent')

    highlight: Optional[str] = attr(name='highlight')
    hidden: Optional[str] = attr(name='hidden')
    
    html: Optional[str] = attr(name='html', max_length=3)

    visible: Optional[str] = attr(name='visible')
    enabled: Optional[str] = attr(name='enabled')
    active: Optional[str] = attr(name='active')
    post_dna: Optional[str] = attr(name='post_dna', max_length=10, regex=r'^(0|[1-9](\d+)?)$')
    DefaultValue: Optional[str] = attr(name='defaultvalue')

    def dict(self, *args, **kwargs):
        
        kwargs["exclude_none"] = True
        return BaseXmlModel.dict(self, *args, **kwargs)
