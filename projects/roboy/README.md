## 1 - Why the ParlAI?
Roboy dialog consists of a state machine. 
personality file contains several states and what they do
if indicated that state has a fallback 
input which can not be parsed is forwarded to the generative model if implemented that way. 

Roboy's fall-back in case it does not know what to answer. 
Embedded in dialogue through...

parser semantic analysis/extraction of information
keine antwort von state nor from parser
option: fall back
input forwarded to generative model through ros

## 2 - Setup
### Prerequisits
- Python 36 environment
- pip3

### Installing ParlAI
Go to the folder you want to have ParlAI in and run the following commands to clone the repository and install ParlAI:
```
git clone https://github.com/Roboy/ParlAI.git
```
```
cd ~/ParlAI
```
```
python setup.py develop
```
This will link the cloned directory to your site-packages. 

This is the recommended installation procedure, as it provides ready access to the examples and allows you to modify anything you might need. This is especially useful if you if you want to submit another task to the repository.

All needed data will be downloaded to ~/ParlAI/data, and any non-data files (such as the MemNN code) if requested will be downloaded to ~/ParlAI/downloads. If you need to clear out the space used by these files, you can safely delete these directories and any files needed will be downloaded again. 

### Further requirements
ParlAI does not install all requirements in setup, some are hidden in the code. For each use case get the following modules as well:

#### Interacting
- [PyTorch](http://pytorch.org/)
- go to `projects/roboy` and run
```
pip install -r requirements.txt
```

#### Training
- [Spacy](https://spacy.io/usage/) (make sure to get module en as well!) 

#### Analysis
- jupyter
- matplotlib

## 3 - Examples

[ParlAI](https://github.com/Roboy/ParlAI/) (pronounced “par-lay”) is a framework for dialog AI research by Facebook, implemented in Python. See their website [http://parl.ai](http://parl.ai) for further docs

ParlAI is described in the following paper:
[“ParlAI: A Dialog Research Software Platform", arXiv:1705.06476](https://arxiv.org/abs/1705.06476), the dataset used is described in the original [PersonaChat](https://arxiv.org/pdf/1801.07243.pdf) paper.

To interact with a pretrained profilememory model (downloaded from model zoo), in `ParlAI` folder run:
```
python projects/convai2/baselines/profilememory/interactive.py 
```

## 4 - Note
The server version runs on ParlAI branch `roboy_server``. (just for testing convenience)

## 5 - Lessons Learned
- there are preinstalled packages abailable for the GCloud setup which makes it way smoother
- ParlAI is kind of a centralized framework, so functions in /core/ for instance work with all the available datasets and architectures. This entails that changes in totally different parts of the code by one of the contributors can prevent an implementation which used to work just fine for you from running. So think and thoroughly test before you merge!
