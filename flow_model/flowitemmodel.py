'''
'''

from typing import Dict
from .flowitemtype import FlowItemType

class FlowItemModel():
  def __init__(self, type: FlowItemType, name: str, params: Dict={}, aliases: Dict={}) -> None:
      self._type = type
      self._name = name
      # Params are defined in ws
      self._params_ws: Dict = params
      # Paramsfrom the item definition
      self._params_def: Dict = None
      # Actual, working params:
      # Values may are:
      # 1. start - from ws definition
      # 2. from update
      self._params: Dict = params
      self._aliases = aliases

  @property
  def itype(self) -> FlowItemType:
    return self._type

  @property
  def name(self) -> str:
    return self._name

  @property
  def params_ws(self) -> Dict:
    return self._params_ws

  @property
  def params_def(self) -> Dict:
    return self._params_def

  @params_def.setter
  def params_def(self, params) -> None:
    self._params_def = params

  @property
  def params(self) -> Dict:
    return self._params

  @params.setter
  def params(self, params) -> None:
    self._params = params

  @property
  def aliases(self) -> Dict:
    return self._aliases
  