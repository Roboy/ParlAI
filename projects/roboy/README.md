## Why the ParlAI?
Roboy's fall-back in case it does not know what to answer. 
Embedded in dialogue through...

## Setup
### Requirements:
- [ParlAI](https://github.com/facebookresearch/ParlAI)
- [ss18_showmaster](https://github.com/Roboy/ss18_showmaster)
- Python 36 environment incl. [PyTorch](http://pytorch.org/)
- jupyter (for analysis)
- matplotlib (for analysis)
- websockets (for ROS)
- further training requirements specified at the end of the according [README](https://github.com/Roboy/ParlAI/tree/master/projects/roboy/train)

### Installing ParlAI

Run the following commands to clone the repository and install ParlAI:

```bash
git clone https://github.com/Roboy/ParlAI.git ~/ParlAI
cd ~/ParlAI; python setup.py develop
```

This will link the cloned directory to your site-packages.

This is the recommended installation procedure, as it provides ready access to the examples and allows you to modify anything you might need. This is especially useful if you if you want to submit another task to the repository.

All needed data will be downloaded to ~/ParlAI/data, and any non-data files (such as the MemNN code) if requested will be downloaded to ~/ParlAI/downloads. If you need to clear out the space used by these files, you can safely delete these directories and any files needed will be downloaded again.

## Examples

[ParlAI](https://github.com/Roboy/ParlAI/) (pronounced “par-lay”) is a framework for dialog AI research by Facebook, implemented in Python. See their website [http://parl.ai](http://parl.ai) for further docs

ParlAI is described in the following paper:
[“ParlAI: A Dialog Research Software Platform", arXiv:1705.06476](https://arxiv.org/abs/1705.06476), the dataset used is described in the original [PersonaChat](https://arxiv.org/pdf/1801.07243.pdf) paper.

To interact with profilememory model (downloaded from model zoo if not available yet), in ParlAI folder run:
```
python projects/convai2/baselines/profilememory/interactive.py 
```

## ParlAI Support
ParlAI is currently maintained by Emily Dinan, Alexander H. Miller, Kurt Shuster, Jack Urbanek and Jason Weston, a very helpful team. If you have any questions, bug reports or feature requests, post on their [Github Issues page](https://github.com/facebookresearch/ParlAI/issues) and issues will usually be resolved within hours (NY time!).

