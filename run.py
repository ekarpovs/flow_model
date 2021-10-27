# Usage:
#   python run.py -w <worksheet full name> [-t no/yes]
# 
import json
import argparse
from typing import Dict, List

from flow_model import FlowModel, FlowItemType, FlowItemModel

# Construct the argument parser and parse the arguments
def parseArgs():
  ap = argparse.ArgumentParser(description="flow model")
  ap.add_argument("-p", "--path", required = True,
	help = "path to the directory with the worksheet")
  ap.add_argument("-n", "--name", required = True,
	help = "the worksheet file name")
  ap.add_argument("-t", "--trace", required = False,
  default="no",
	help = "print output")
  
  args = ap.parse_args()   
  kwargs = dict((k,v) for k,v in vars(args).items() if k!="message_type")
  return kwargs

def load_worksheet(ffn: str) -> List[Dict]:
    # load the worksheet from the path 
    with open(ffn, 'rt') as ws:
      worksheet = json.load(ws)
    return worksheet

# Main function
def main(**kwargs):
  path = kwargs.get('path')
  name = kwargs.get('name')
  ffn = f'{path}/{name}.json'
  ws = load_worksheet(ffn)
  model = FlowModel(path, name, ws)
  print(model.info)
  print(model.name)
  print(model.path)


# Entry point
if __name__ == "__main__":
    kwargs = parseArgs()
    main(**kwargs) 
