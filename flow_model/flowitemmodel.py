'''
'''

from .flowitemtype import FlowItemType

class FlowItemModel():
  def __init__(self, type: FlowItemType=FlowItemType.EXEC, name: str='', params: dict=None, aliases: dict=None) -> None:
      self._type = type
      self._name = name
      self._params = params
      self._aliases = aliases

  @property
  def itype(self) -> FlowItemType:
    return self._type

  @property
  def name(self) -> str:
    return self._name

  @property
  def params(self) -> dict:
    return self._params

  @params.setter
  def params(self, params: dict = {}) -> None:
    self._params = params
    return

  @property
  def aliases(self) -> dict:
    return self._aliases
  
  @aliases.setter
  def aliases(self, aliases: dict = {}) -> None:
    self._aliases = aliases
    return
