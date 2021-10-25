'''
'''
import json
from typing import List, Dict

from .flowitemtype import FlowItemType
from .flowitemmodel import FlowItemModel

BEGIN_FLOW_MARKER = {"stm": "glbstm.begin"}
END_FLOW_MARKER = {"stm": "glbstm.end"}

class FlowModel():
  def __init__(self, path: str) -> None:
      self._path: str = path
      self._name: str = ''
      self._info: str = ''
      self._items: List[FlowItemModel] = []
      return
      

  def _parse(self, name: str, flow: List[Dict]) -> None:
    self.name = name
    item = FlowItemModel(FlowItemType.STM_BEGIN, 'glbstm.begin')
    self._items.append(item)
    for step in flow:
      if 'info' in step:
        self.info = step.get('info')
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
      self._items.append(item)
    item = FlowItemModel(FlowItemType.STM_END, 'glbstm.end')
    self._items.append(item)
    return

  @property
  def path(self) -> str:
    return self._path

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str) ->None:
    self._name = name
    return

  @property
  def info(self) -> str:
    return self._info

  @info.setter
  def info(self, info: str) ->None:
    self._info = info
    return
 
  @property
  def items(self) -> List[FlowItemModel]:
    return self._items

  @property
  def loaded(self) -> bool:
    return len(self._items) > 0


  def get_flow_item(self, key: str) -> Dict:
    return self._items.get(key, None)


  def load_worksheet(self, name: str) -> None:
    # load the worksheet from the path 
    ffn = f'{self.path}/{name}.json'
    with open(ffn, 'rt') as ws:
      worksheet = json.load(ws)
      self._parse(name, worksheet)
    return

