# /bin/bash
export PYTHONPATH=
export PATH=~/anaconda3/bin:$PATH

## get this to point to venv for ParlAI
source ~/Documents/Roboy/venv_ParlAI/bin/activate

python projects/convai2/baselines/profilememory/interactive.py
