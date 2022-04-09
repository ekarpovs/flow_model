# Workshop Flow Model

## It is a part of the [Image Processing Workshop](https://github.com/ekarpovs/image-processing-workshop) project. The model reads and stores a flow defenition (worksheet)

### File system structure

    Anywhere in a file system:
_____
    |__ /data/ __ files for processing
    |
    

    |__ /flow_model/ The project files
    |

## Local Installation

```bash
cd flow_model
pip install -e . --use-feature=in-tree-build

```

## Test

```bash
python run.py -d <worksheet path> -f <worksheet name>
```
