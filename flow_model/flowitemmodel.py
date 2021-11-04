'''
'''

from typing import Dict, List
from .flowitemtype import FlowItemType

class FlowItemModel():
  def __init__(self, type: FlowItemType, name: str, params_ws: Dict={}, aliases: Dict={}) -> None:
      self._type = type
      self._name = name
      # Params are defined in ws
      self._params_ws: Dict = params_ws
      # Params from the item definition
      self._params_def: List[Dict] = None
      # Actual, working params:
      # Values may are:
      # 1. start - from ws definition
      # 2. from update
      self._params: Dict = params_ws
      # input/output references from the item definition
      self._inrefs_def: List[str] = None
      self._outrefs_def: List[str] = None
      self._aliases: Dict[str, str] = aliases

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
  def inrefs_def(self) -> List[str]:
    return self._inrefs_def

  @inrefs_def.setter
  def inrefs_def(self, inrefs: List[str]) -> None:
    self._inrefs_def = inrefs
    return

  @property
  def outrefs_def(self) -> List[str]:
    return self._outrefs_def

  @outrefs_def.setter
  def outrefs_def(self, outrefs: List[str]) -> None:
    self._outrefs_def = outrefs
    return

  @property
  def aliases(self) -> Dict[str, str]:
    return self._aliases
  