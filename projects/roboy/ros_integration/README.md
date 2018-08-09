## Setup
### Requirements
- [ROS Kinetic](http://wiki.ros.org/kinetic)
- [ROSbridge](http://wiki.ros.org/rosbridge_suite)
- [Catkin Workspace](https://github.com/Roboy)

### Prerequisites

- you need a full model setup. From scratch, the easiest way to achieve this is to run
```
python projects/convai2/baselines/profilememory/interactive.py 
```

## ROS Communication 101

### 1. Rosbridge Websocket
- in terminal, run 
```
roslaunch rosbridge_server rosbridge_websocket.launch
```

### 2. Start Model
- in a new terminal
- activate the python 36 environment you set up when preparing to work with ParlAI as described [here](https://github.com/Roboy/ParlAI/)
- in `ss18_showmaster/ParlAI/projects/roboy/ros_integration` run 
```
python gnlp_ros_srv.py
```

### 3. Test the Service
- in another terminal
- get available services through running `rosservice list`
- run 
```
source (catkin_ws)/devel/setup.bash
```
with (catkin_ws) being the location of your catkin workspace such as `Documents/Roboy/catkin_ws`
```
rosservice call /roboy/cognition/generative_nlp/answer "text_input: 'hello'"
```

## ROS Communication 102
How to fix stuff

### 1. Edit IP adress in last line 
- (local host: 127.0.0.1:11311)
```
gedit ~/.bashrc
```
### 2. Source it 
```
source ~/.bashrc
```
### 3. run bash
```
source Documents/Roboy/catkin_ws/devel/setup.bash
```
### 4. launch ROS service 
- (as in step 101.1)
```
roslaunch rosbridge_server rosbridge_websocket.launch
```
### 5. Update IP adress 
- in gnlp_ros_srv.py, then launch as in setp 101.2


## If you want to further work on ParlAI

Roboys ROS-integration is derived from what happens through running `python projects/convai2/baselines/profilememory/interactive.py`.

### Data flow
In `projects/convai2/baselines/profilememory/interactive.py` setup is done for interacting with a profilememory model, the actual interaction is defined in `parlai/scripts/interactive.py`.  We want to manipulate the world the agents interact in to allow I/O through ROS. 

#### Extract model response
`core/worlds.py` is where `ROS_worlds.py` is derived from. There, I changed [`def parlay(self)`](https://github.com/Roboy/ParlAI/blob/56b0d6ad5962cec0465d37a74e6211b12c60463e/parlai/core/worlds.py#L237-L245) function to return the model response to `gnlp_ros_srv.py` through adding a `sentence` variable. 

#### Implement personality
`roboys_persona_seq2seq.py` is a slight modification of  `projects/personachat/persona_seq2seq.py` which has Roboys personality integrated in line [1602](https://github.com/Roboy/ParlAI/blob/b9844eaf83b5cb5c0fcb0d00c7fd68dcf28ea7cd/projects/roboy/ros_integration/roboys_persona_seq2seq.py#L1602), an example is shown below. 
```
self.persona_given = 'I am a robot.\nI cant walk.\nI own a tricycle.\nI love my team.\n'
```

If you want to do changes / add new sentences to `self.persona_given` please keep in mind, that words might be 'out of dict'. If they are not represented in the dict-file coming with the model, they are replaced by the unknown token `__UNK__` before being handed on to the model. That way, if you insert something like `my name is roboy\n` the model will see `my name is __UNK__\n` and reply with whatever it thinks will fit best, in this case probably a name it has learned before. You can circumvent this by replacing an entry in the dict file. This works best when words are from the same 'intuitive category', so in the example given replace a name you find in the dict file by roboy (make sure to stick with the appropriate upper-case/lower-case convention). !Do not attempt to add an entry to the dict file!

#### How it works together
The main script for the ROS-integration essentially is a modification of the [earlier used implementation](https://github.com/Roboy/DeepQA/blob/master/gnlp_ros_srv.py). [Setup is hard-coded](https://github.com/Roboy/ParlAI/blob/fc5fe7540dedf993765522a9fa88ca0bec7037d1/projects/roboy/ros_integration/gnlp_ros_srv.py#L39-L57) as extractet from `opt`-variable in [`profilememory/interactive.py`](https://github.com/Roboy/ParlAI/blob/roboy_devel/projects/convai2/baselines/profilememory/interactive.py). 
[Lines 41 to 45 of `parlai/scripts/interactive.py`](https://github.com/Roboy/ParlAI/blob/fc5fe7540dedf993765522a9fa88ca0bec7037d1/parlai/scripts/interactive.py#L41-L45) form the basis of `gnlp_ros_service.py` as can be seen below. 
```
opt['task'] = 'parlai.agents.local_human.local_human:LocalHumanAgent'

# Create model and assign it to the specified task
agent = create_agent(opt, requireModelExists=True)
world = create_task(opt, agent)
```

Instead of `core/worlds.py` we import `ROS_worlds.py` in [line 37](https://github.com/Roboy/ParlAI/blob/fc5fe7540dedf993765522a9fa88ca0bec7037d1/projects/roboy/ros_integration/gnlp_ros_srv.py#L37). 
Instead of calling `projects.roboy.ros_integration.persona_seq2seq:PersonachatSeqseqAgentSplit` in [line 33](https://github.com/Roboy/ParlAI/blob/fc5fe7540dedf993765522a9fa88ca0bec7037d1/projects/roboy/ros_integration/gnlp_ros_srv.py#L33), we call roboys version of it.  
