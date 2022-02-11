'''
'''

import copy
from typing import Dict, List
from .flowitemtype import FlowItemType

class FlowItemModel():
  def __init__(self, type: FlowItemType, name: str, title: str='', params_ws: Dict={}, links: Dict={}) -> None:
      self._type = type
      self._name = name
      self._title = title
      # Params are defined in ws
      self._params_ws: Dict = params_ws
      # Params from the item definition
      self._params_def: List[Dict] = None
      # Actual, working params:
      # Values may are:
      # 1. start - from ws definition
      # 2. from update
      self._params: Dict = copy.deepcopy(self._params_ws)
      # input/output references from the item definition
      # self._inrefs_def: List[str] = None
      # self._outrefs_def: List[str] = None
      self._links: Dict[str, str] = links

  @property
  def itype(self) -> FlowItemType:
    return self._type

  @property
  def name(self) -> str:
    return self._name

  @property
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title) -> None:
    self._title = title
    return 
    
  @property
  def params_ws(self) -> Dict:
    return self._params_ws

  @property
  def params_def(self) -> List[Dict]:
    return self._params_def

  @params_def.setter
  def params_def(self, params: List[Dict]) -> None:
    self._params_def = params

  @property
  def params(self) -> Dict:
    return self._params

  @params.setter
  def params(self, params) -> None:
    self._params = params

  @property
  def links(self) -> Dict[str, str]:
    return self._links
  