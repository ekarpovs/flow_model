# Usage:
#   python run.py -w <worksheet full name> [-t no/yes]
# 

import argparse

from flow_model import FlowModel, FlowItemType, FlowItemModel

# Construct the argument parser and parse the arguments
def parseArgs():
  ap = argparse.ArgumentParser(description="flow model")
  ap.add_argument("-d", "--dir", required = True,
	help = "path to the directory with the worksheet")
  ap.add_argument("-f", "--file", required = True,
	help = "the worksheet file name")
  ap.add_argument("-t", "--trace", required = False,
  default="no",
	help = "print output")
  
  args = ap.parse_args()   
  kwargs = dict((k,v) for k,v in vars(args).items() if k!="message_type")
  return kwargs


# Main function
def main(**kwargs): 
  model = FlowModel(kwargs.get('dir'))
  model.load_worksheet(kwargs.get('file'))
  print(model.info)
  print(model.name)
  print(model.path)


# Entry point
if __name__ == "__main__":
    kwargs = parseArgs()
    main(**kwargs) 
