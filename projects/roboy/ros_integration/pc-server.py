import procbridge as p
# from procbridge import procbridge
import sys
import os
import logging
import stringcase
import re


if __name__ == '__main__':

    host = '127.0.0.1'
    port = 8877

    def cap(match):
        return(match.group().capitalize())


    def clean(s):
        p = re.compile(r'(?<=[\.\?!]\s)(\w+)')
        ret = p.sub(cap, re.sub(r'\s([?.!"](?:\s|$))', r'\1', s))
        return ret[0].upper() + ret[1:]


    # define request handler
    def request_handler(api: str, arg: dict) -> dict:
        sentence = arg['text_input']
        logging.info("received " + sentence)
        return {'result': clean(world.parley(sentence))}

    ros_integration_home = os.path.dirname(os.path.realpath(__file__))
    download_path = ros_integration_home + '/../../../downloads'
    datapath = ros_integration_home + '/../../../data'

    #model_path = ros_integration_home + '/data/models/convai2/profilememory/180812_1405'
    #model_file = model_path + '/roboy_profilemem'
    #dict_file = model_path + '/roboy_profilemem.dict'

    # Pretrained
    model_file = ros_integration_home + '/../../../data/models/convai2/profilememory/profilememory_convai2_model'
    dict_file = ros_integration_home + '/../../../data/models/convai2/profilememory/profilememory_convai2.dict'

    personachat_code = 'projects.roboy.ros_integration.roboys_persona_seq2seq:PersonachatSeqseqAgentSplit'

    ### prepare the model ###
    from parlai.core.agents import create_agent
    from ROS_worlds import create_task

    opt = {'task': None, 'download_path': download_path, \
            'datatype': 'train', 'image_mode': 'raw', 'numthreads': 1, 'hide_labels': False, 'batchsize': 1, \
            'include_labels': True, 'datapath': datapath, \
            'model': personachat_code, \
            'model_file': model_file, \
            'dict_class': None, 'display_examples': False, 'image_size': 256, 'image_cropsize': 224, \
            'dict_file': dict_file, \
            'dict_initpath': None, 'dict_language': 'english', 'dict_max_ngram_size': -1, 'dict_minfreq': 0, \
            'dict_maxtokens': -1, 'dict_nulltoken': '__NULL__', 'dict_starttoken': '__START__', 'dict_endtoken': '__END__', \
            'dict_unktoken': '__UNK__', 'dict_tokenizer': 'split', 'dict_lower': False, 'hiddensize': 1024, \
            'embeddingsize': 300, 'numlayers': 2, 'learningrate': 0.5, 'dropout': 0.1, 'bidirectional': False, \
            'attention': 'general', 'no_cuda': False, 'gpu': -1, 'rank_candidates': False, 'truncate': -1, 'encoder': 'lstm', \
            'decoder': 'same', 'optimizer': 'adam', 'personachat_useprevdialog': True, 'personachat_printattn': False, \
            'personachat_attnsentlevel': True, 'personachat_sharelt': False, 'personachat_reweight': 'use', \
            'personachat_guidesoftmax': False, 'personachat_newsetting': '', 'personachat_interact': False, \
            'personachat_pdmn': False, 'personachat_tfidfperp': False, 'personachat_learnreweight': True, \
            'personachat_embshareonly_pm_dec': False, 'personachat_s2sinit': False, 'interactive_mode': True, \
            'use_persona': 'self', 'parlai_home': ros_integration_home + '/../../../', 'override': {}, \
            'starttime': 'Jun15_16-58'}
    opt['model_type'] = 'profilememory' # for builder

    opt['task'] = 'parlai.agents.local_human.local_human:LocalHumanAgent'

    # Create model and assign it to the specified task
    agent = create_agent(opt, requireModelExists=True)
    world = create_task(opt, agent)
    #### model ready to go ####

    logging.info("Service /roboy/cognition/generative_nlp/answer is ready")

    # start socket server
    server = p.procbridge.ProcBridgeServer(host, port, request_handler)
    server.start()
    print('listening...')

    try:
        for line in sys.stdin:
            if line.strip() == 'exit':
                break
    except KeyboardInterrupt:
        pass

    server.stop()
print('bye!')
