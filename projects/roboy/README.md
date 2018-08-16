## 1 - Why the ParlAI?
Roboy dialog system essentially is a state machine. A personality file contains several states and what they do. Each state can make use of an optional fallback position. This is triggered when input can not be parsed. Then, input will be redirected to a generative model to create an output. [ParlAI](https://github.com/Roboy/ParlAI/) (pronounced “par-lay”) is the framework behind this generative model, implemented in Python and designed for dialog AI research by Facebook. See [their website http://parl.ai](http://parl.ai) for further docs.

ParlAI is described in the following paper: [“ParlAI: A Dialog Research Software Platform"](https://arxiv.org/abs/1705.06476), the dataset used is described in the original [PersonaChat](https://arxiv.org/pdf/1801.07243.pdf) paper. ParlAI is the successor of [Roboy/DeepQA](https://github.com/Roboy/DeepQA).

Roboy is using a so-called profilememory network, which essentially consists of a sequence to sequence neural net using LSTMs. An attention mechanism affects outputs with respect to the conversation history. Furthermore, a consistent personality can be included which also affects outputs. 

Pitfalls: Profilememory is the original implementation coming with the personachat dataset. It has been choosen as it can _memorize_ a profile. The idea behind it is to influence outputs in a way where the net acts as it was someone, Roboy in our case of course. According to [ParlAI issue #1066](https://github.com/facebookresearch/ParlAI/issues/1066) the model is not as powerful as other implementations provided by ParlAI. Anyhow, it suits our case. So if you want to win the ConvAI challenge better go for a different one. 


The three major advantages of the profilmemory implementation over the previous DeepQA implementation are:

- DeepQA consists of a pure seq2seq model, so it would give the exact same reply to a specific input observed. Profilememory takes the conversational history into account through attention.
- Through integrating a consistent personality to influence the softmax layer, we are also able to keep Roboy more ... even in its fallback sate. 
- The personachat dataset is originating from actual conversations humans had with each other. This results in a more realistic chitchat in comparison to the DeepQA implementation as that was trained on a movie subtitle database resulting in a very dramatic behavior of the model. 



## 2 - How the ParlAI
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

## 3 - Try the ParlAI

To interact with a pretrained profilememory model (downloaded from model zoo), in `ParlAI` folder run:
```
python projects/convai2/baselines/profilememory/interactive.py 
```

## 4 - Note the ParlAI
- ParlAI is forked from [facebookresearch/ParlAI](https://github.com/facebookresearch/ParlAI), we do not use their devel branch. 
- Development is on ParlAI branch `roboy_devel`.
- The server version runs on ParlAI branch `roboy_server`. 
- The nuke version runs on ParlAI branch `roboy_nuke`. 
    This mainly concernes paths but is also convenient if you want to make some changes to certain parts only. 
- As of August 16th, 2018, ParlAI has ropped support for the profilememory implementation in the ConvAI2 challenge and removed the code from the `projects/convai2/baselines/profilememory/` directory. However, we want to use the convai2 personachat dataset as it contains more samples than the original personachat (`projects/personachat`) implementation. The good news is, the personachat implementation will still be supported, just not in the scope of the ConvAI2 challenge. So implementations in `projects/personachat` will be kept updated. The thing we need to care about is the dataset, which is integrated through setting `task='convai2:self'` in the training script. A copy of the contents of the `projects/convai2/baselines/profilememory` directory is in `projects/roboy/profilememory/`. 


