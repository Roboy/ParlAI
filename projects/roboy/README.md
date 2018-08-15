## 1 - Why the ParlAI?
Roboy dialog system essentially is a state machine. A personality file contains several states and what they do. Each state can make use of an optional fallback position. This is triggered when input can not be parsed. Then, input will be redirected to a generative model to create an output. [ParlAI](https://github.com/Roboy/ParlAI/) (pronounced “par-lay”) is the framework behind this generative model, implemented in Python and designed for dialog AI research by Facebook. See their website [http://parl.ai](http://parl.ai) for further docs.

ParlAI is described in the following paper: [“ParlAI: A Dialog Research Software Platform", arXiv:1705.06476](https://arxiv.org/abs/1705.06476), the dataset used is described in the original [PersonaChat](https://arxiv.org/pdf/1801.07243.pdf) paper.

## 2- How the ParlAI
Roboy is using a so-called profilememory neural net, which essentially consists of a sequence to sequence RNN with LSTMs. An attention mechanism is used to influence outputs in a way ... make it Roboy. The sentences given  are "XYZ". If too many personality sentences are specified, the influence of each will decrease and therefore the performance of the model.   

You will find something like ...

Pitfalls: Profilememory is the original implementation coming with the personachat dataset. It has been choosen as it can _memorize_ a profile. The idea behind it is to influence outputs in a way where the net acts as it was someone, Roboy in our case of course. According to [ParlAI issue #1066](https://github.com/facebookresearch/ParlAI/issues/1066) the model is not as powerful as other implementations provided by ParlAI. Anyhow, it suits our case. So if you want to win the ConvAI challenge better go for a different one. 

## 3 - Setup the ParlAI
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
This will link the cloned directory to your site-packages and is the recommended installation procedure, as it provides ready access to the examples and allows you to modify anything you might need. This is especially useful if you if you want to submit another task to the repository.

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

## 4 - Try the ParlAI

To interact with a pretrained profilememory model (downloaded from model zoo), in `ParlAI` folder run:
```
python projects/convai2/baselines/profilememory/interactive.py 
```

## 5 - Note the ParlAI
- ParlAI is forked from [facebookresearch/ParlAI](https://github.com/facebookresearch/ParlAI), we do not use their devel branch. 
- Development is on ParlAI branch `roboy_devel`.
- The server version runs on ParlAI branch `roboy_server`. 
- The nuke version runs on ParlAI branch `roboy_nuke`. 
    This mainly concernes paths but is also convenient if you want to make some changes to certain parts only. 

## 6 - Lessons Learned 
- there are preinstalled packages abailable for the GCloud setup which makes it way smoother
- ParlAI is kind of a centralized framework, so functions in /core/ for instance work with all the available datasets and architectures. This entails that changes in totally different parts of the code by one of the contributors can prevent an implementation which used to work just fine for you from running. So think and thoroughly test before you merge!
- Do not use too many personality phrases.
