# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
"""Train model for ppl metric with pre-selected parameters.
These parameters have some variance in their final perplexity, but they were
used to achieve the pre-trained model.
"""

# only used for very basic setup. Use shell script for hyperparameter definition

from parlai.scripts.train_model import setup_args, TrainLoop


if __name__ == '__main__':
    parser = setup_args()
    parser.set_defaults(
        task='convai2:self',
        model='projects.personachat.persona_seq2seq:PersonachatSeqseqAgentSplit',
        model_file='/tmp/roboy_profilemem',
        dict_lower=True,
        dict_include_valid=True,
        dict_maxexs=-1,
        datatype='train',
        batchsize=64, # CUDA runs out of memory otherwise
        encoder='lstm',
        learningrate=0.001,
        numlayers=2,
        hiddensize=1024,
        dropout=0.2,
        attention='general',
        personachat_attnsentlevel=True,
        personachat_sharelt=True,
        personachat_learnreweight=True,
        personachat_reweight='use',
        truncate=100, # Truncate (default 100, -1 gives minimum length):
        rank_candidates=True,
        validation_every_n_secs=180,
        validation_metric='ppl',     #or: f1 max or ppl min
        validation_metric_mode='min',
        validation_patience=10,
        log_every_n_secs=10,
    )
    TrainLoop(parser.parse_args()).train()
