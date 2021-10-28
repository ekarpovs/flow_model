from typing import List, Dict, Tuple

from .flowitemtype import FlowItemType
from .flowitemmodel import FlowItemModel

BEGIN_FLOW_MARKER = {"stm": "glbstm.begin"}
END_FLOW_MARKER = {"stm": "glbstm.end"}

class FlowModel():
  '''
  Flow model
  '''

  def __init__(self, path: str, name: str, worksheet: List[Dict]) -> None:
      self._path: str = path
      self._name: str = name
      (self._info, self._items) = self._parse(worksheet)
      return
      
  @property
  def path(self) -> str:
    return self._path

  @property
  def name(self) -> str:
    return self._name

  @property
  def info(self) -> str:
    return self._info

  @property
  def items(self) -> List[FlowItemModel]:
    return self._items

  @property
  def loaded(self) -> bool:
    return len(self._items) > 0

  def get_item(self, name) -> FlowItemModel:
    for item in self.items:
      if item.name == name:
        return item
    return None
    
  @staticmethod
  def _parse(worksheet: List[Dict]) -> Tuple[str, List[FlowItemModel]]:
    info = ''
    items: List[FlowItemModel] = []
    item = FlowItemModel(FlowItemType.STM_BEGIN, 'glbstm.begin')
    items.append(item)
    for step in worksheet:
      if 'info' in step:
        info = step.get('info')
        continue
      type = None
      iname = ''
      params = {}
      aliases = {}
      if 'exec' in step:
        type = FlowItemType.EXEC
        iname = step.get('exec')
      elif 'stm' in step:
        type = FlowItemType.STM_BEGIN
        iname = step.get('stm')
      if 'params' in step:
        params = step.get('params')
      if 'aliases' in step:
        aliases = step.get('aliases')
      item = FlowItemModel(type, iname, params, aliases)
      items.append(item)
    item = FlowItemModel(FlowItemType.STM_END, 'glbstm.end')
    items.append(item)
    return (info, items)
