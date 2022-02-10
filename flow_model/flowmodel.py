from typing import List, Dict, Tuple

from .flowitemtype import FlowItemType
from .flowitemmodel import FlowItemModel

class FlowModel():
  '''
  Flow model
  '''

  def __init__(self, worksheet: List[Dict]) -> None:
    # self._worksheet = worksheet
    self._info: str = ''
    self._items: List[FlowItemModel] = []   
    self._build(worksheet)
    return
  
  @property
  def info(self) -> str:
    return self._info

  @info.setter
  def info(self, info) -> None:
    self._info = info
    return

  @property
  def items(self) -> List[FlowItemModel]:
    return self._items

  @property
  def loaded(self) -> bool:
    return len(self._items) > 0

  def get_item(self, idx: int) -> FlowItemModel:
    return self.items[idx]

  def set_item(self, idx: int, item: FlowItemModel) -> None:
    self.items.insert(idx, item)
    return

  def remove_item(self, idx) -> None:
    self.items.pop(idx)
    return

  def get_item_params(self, idx: int) -> Dict:
    return self.items[idx].params

  def set_item_params(self, idx: int, params) -> None:
    self.items[idx].params = params
    return


  def _build(self, worksheet: List[Dict]) -> None:
    for step in worksheet:
      if 'info' in step:
        self._info = step.get('info')
        continue
      type = None
      iname = ''
      ititle = ''
      params = {}
      links = {}
      type = FlowItemType.EXEC
      iname = step.get('exec')
      ititle = step.get('title', '')
      if 'params' in step:
        params = step.get('params')
      if 'links' in step:
        links = step.get('links')
      item = FlowItemModel(type, iname, ititle, params, links)
      self.items.append(item)
    return

  def get_as_ws(self) -> List[Dict]:
    ws = [{"info": self.info}]   
    for item in self.items:
      iname = item.name
      ws_item = {"exec": iname}
      ititle = item.title
      ws_item["title"] = ititle
      iparams = item.params
      if len(iparams)> 0:
        ws_item["params"] = iparams
      ilinks = item.links
      if len(ilinks)> 0:
        ws_item["links"] = ilinks
      ws.append(ws_item)
    return ws