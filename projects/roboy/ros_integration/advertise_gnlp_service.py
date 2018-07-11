# /bin/bash
export PYTHONPATH=
export PATH=~/anaconda3/bin:$PATH

source activate python35

python gnlp_ros_srv.py --modelTag pretrainedv2 --test ros



## get this to point to venv for ParlAI
# source activate python36

#python3 projects/convai2/baselines/profilememory/interactive.py


#1. Rosbridge websocket
#roslaunch rosbridge_server rosbridge_websocket.launch 
#2. In a new terminal start model 
#python gnlp_ros_srv.py
#3. In another terminal test the service
#source (catkin_ws)/devel/setup.bash
#rosservice call /roboy/cognition/generative_nlp/answer "text_input: 'hello'" 

