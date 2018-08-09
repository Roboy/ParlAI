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
### 4. launch ROS service as in step 101.1
```
roslaunch rosbridge_server rosbridge_websocket.launch
```
### 5. Update IP adress in gnlp_ros_srv.py 


## If you want to do further work on ParlAI

Roboys ROS-integration is derived from what happens through running `python projects/convai2/baselines/profilememory/interactive.py`.

### Data flow:

#### Extract model response
`core/agents.py`
`core/worlds.py` is where ROS_worlds.py is derived from. There, I changed the [`def parlay()`(https://github.com/Roboy/ParlAI/blob/56b0d6ad5962cec0465d37a74e6211b12c60463e/parlai/core/worlds.py#L237-L245) function to return the model response to `gnlp_ros_srv.py`. 
`projects/personachat/seq2seq.py`

#### Implement personality

#### Error handling
