'''
'''

from typing import Dict
from .flowitemtype import FlowItemType

class FlowItemModel():
  def __init__(self, type: FlowItemType=FlowItemType.EXEC, name: str='', params: Dict={}, aliases: Dict={}) -> None:
      self._type = type
      self._name = name
      self._params: Dict = params
      self._aliases = aliases

  @property
  def itype(self) -> FlowItemType:
    return self._type

  @property
  def name(self) -> str:
    return self._name

  @property
  def params(self) -> Dict:
    return self._params

  @params.setter
  def params(self, params: Dict = {}) -> None:
    self._params = params
    return

  @property
  def aliases(self) -> Dict:
    return self._aliases
  
  @aliases.setter
  def aliases(self, aliases: Dict = {}) -> None:
    self._aliases = aliases
    return
