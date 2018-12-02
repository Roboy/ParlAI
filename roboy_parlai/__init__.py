#!/usr/bin/env python3

import os
from os.path import realpath, dirname, join
module_path = dirname(realpath(__file__))
os.environ['PARLAI_HOME'] = module_path

from roboy_parlai.projects.personachat.persona_seq2seq import PersonachatSeqseqAgentSplit
from parlai.core.build_data import download_models
from parlai.core.params import ParlaiParser

# model_name = 'profilememory_convai2_model'
# dict_name = 'profilememory_convai2.dict'

model_name = \
  'profilememory_learnreweight_sharelt_encdropout0.4_s2s_usepersona_self_useall_attn_general_lstm_1024_1_1e-3_0.1'
dict_name = 'fulldict.dict'

os.environ['PARLAI_HOME'] = module_path
parser = ParlaiParser()
PersonachatSeqseqAgentSplit.add_cmdline_args(parser)
parser.set_defaults(
    download_path=join(module_path, 'downloads'),
    datapath=join(module_path, 'data'),
    # model_type="profile_memory",
    model='roboy_parlai.projects.personachat.persona_seq2seq:PersonachatSeqseqAgentSplit',
    model_file=join(module_path, 'data', 'models', 'personachat', model_name),
    dict_file=join(module_path, 'data', 'models', 'personachat', dict_name),
    personachat_useprevdialog=True,
    interactive_mode=True,
    use_persona='self'
)
opt = parser.parse_args([])

download_models(opt, [model_name, dict_name], 'personachat')
agent = PersonachatSeqseqAgentSplit(opt)


def wildtalk(text_input: str) -> str:
    agent.observe({'text': text_input, 'episode_done': False})
    agent.persona_given = ""
    return agent.act()['text']


if __name__ == '__main__':
    while True:
        text_input = input("> ")
        print(wildtalk(text_input))
