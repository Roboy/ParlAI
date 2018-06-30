#!/bin/bash
# clear

python3 train_roboy.py --dict-file models:convai2/profilememory/profilememory_convai2.dict -hs 1024 -emb 300 -nl 3 -bs 128 -lr 0.001 -dr 0.5 -tr -1 -dec same -opt adam -ltim 10 -vtim 180 -vme 1000 -vp 50 -vmt f1 -vmm max -vcut 1.0 -dbf True -stim 900 &>../data/models/convai2/profilememory/profilememory.txt

#
############################# Legend #############################
############################# Model #############################
# Model
#-m 'projects.personachat.persona_seq2seq:PersonachatSeqseqAgentSplit'\
# Task: define personachat task
#-t 'personachat:self'\
# Model file location
#-mf '/tmp/profilememconvai2'\
############################# Seq2Seq Arguments #############################
# size of the hidden layers (default 1024):
#-hs 1024\
# size of the token embeddings (default 300):
#-emb 300\
# number of hidden layers (default 2):
#-nl 2\
# learning rate (default 0.5):
#-lr 0.001\
# dropout rate (default 0.1):
#-dr 0.2\
# Attention (default None):'None, concat, general, local. If local,
# something like "local,N" should be the keyword,
# where N stands for specified attention length
# while decoding
#-att general\
# deisable GPUs even if available (default False):
#--no-cuda False\
# which GPU device to use (default -1):
#--gpu -1\
# Rank (default: FAlse): 'rank candidates if available. this is done by'
# computing the mean score per token for each '
# candidate and selecting the highest scoring.'
#-rc False\
# Truncate (default 100): 'truncate input & output lengths to speed up '
# training (may reduce accuracy). This fixes all '
# input and output to have a maximum length and to '
# be similar in length to one another by throwing '
# away extra tokens. This reduces the total amount '
# of padding in the batches.'
#-tr 100\
# Encoder (default lstm):
#-enc lstm\
# Decoder (default same, choice: shared): 'Choose between different decoder modules. '
# Default "same" uses same class as encoder, '
# while "shared" also uses the same weights.'
#-dec same\
# Optimizer (default adam): Choose between pytorch optimizers. '
# Any member of torch.optim is valid and will '
# be used with default params except learning
#-opt adam\
############################# Personachat #############################
# interact during validation?!
#--personachat_interact False
# share lookup table among self.lt, self.lt_per, self.e2o (default False):
#--personachat_sharelt True\
# helps print nicer text during interactive mode
#--interactive-mode False\
#--personachat_attnsentlevel True\
#--personachat_reweight use\
#--personachat_learnreweight True\
############################# arguments from scripts/train_model.py: #############################
# evaltask
#-et\
# display examples:
#--display-examples False\
# train n epochs (std -1):
#-eps -1\
# max train time: (std 28800)
#-ttim -1\
# log every n seconds (std 10):
#-ltim 10\
# validate every n seconds: (std 900)
#-vtim 150\
# save every n seconds:
#-stim -1\
# save after validation:
#-sval False\
# max examples to use during validation (-1 uses all, std 100000):
#-vme 10000\
# validation patience -> training over after not achieving better validation n times (std -1):
#-vp 10\
# validation metric (std accuracy):
#-vmt accuracy\
# validation metric mode (std max):
#-vmm max\
# validation-cutoff
#-vcut 1.0\
# dict-build-first
#-dbf True\
# load-from-checkpoint
#-lfc False\
# Logging
# >& ../../../ParlAI/data/models/convai2/profilememory/profilememory_log.txt
#| tee data/models/convai2/profilememory/profilememory.log
