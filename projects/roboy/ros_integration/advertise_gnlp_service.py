# /bin/bash
export PYTHONPATH=
export PATH=~/anaconda3/bin:$PATH

## get this to point to venv for ParlAI
source /home/roboy/workspace/venv_ParlAI/bin/activate

python gnlp_ros_srv.py
