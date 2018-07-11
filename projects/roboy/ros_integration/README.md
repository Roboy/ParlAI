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
- in `ss18_showmaster/ParlAI/ros_integration` run 
```
python gnlp_ros_srv.py
```

### 3. Test the Service
- in another terminal
- get available services through running `rosservice list`
- run 
```
(catkin_ws)/devel/setup.bash
```
with (catkin_ws) being the location of your catkin workspace such as `Documents/Roboy/catkin_ws`
```
rosservice call /roboy/cognition/generative_nlp/answer "text_input: 'hello'"
```
