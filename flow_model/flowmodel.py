from typing import List, Dict, Tuple

from .flowitemtype import FlowItemType
from .flowitemmodel import FlowItemModel

class FlowModel():
  '''
  Flow model
  '''

  def __init__(self, worksheet: List[Dict]) -> None:
      (self._info, self._items) = self._parse(worksheet)
      return
      
  @property
  def info(self) -> str:
    return self._info

  @property
  def items(self) -> List[FlowItemModel]:
    return self._items

  @property
  def loaded(self) -> bool:
    return len(self._items) > 0

  def get_item(self, idx: int) -> FlowItemModel:
    return self.items[idx]

  def set_item(self, idx: int, item: FlowItemModel) -> None:
    return  self.items.insert(idx, item)

  def remove_item(self, idx) -> None:
    self.items.pop(idx)
    return

  def get_item_params(self, idx: int) -> Dict:
    return self.items[idx].params

  def set_item_params(self, idx: int, params) -> None:
    self.items[idx].params = params
    return


  @staticmethod
  def _parse(worksheet: List[Dict]) -> Tuple[str, List[FlowItemModel]]:
    info = ''
    items: List[FlowItemModel] = []
    for step in worksheet:
      if 'info' in step:
        info = step.get('info')
        continue
      type = None
      iname = ''
      params = {}
      aliases = {}
      type = FlowItemType.EXEC
      iname = step.get('exec')
      if 'params' in step:
        params = step.get('params')
      if 'aliases' in step:
        aliases = step.get('aliases')
      item = FlowItemModel(type, iname, params, aliases)
      items.append(item)
    return (info, items)
