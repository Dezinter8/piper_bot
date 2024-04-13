# Piper simulation

## Pre requirements

- xacro
- joint-state-publisher
- gazebo

Install those using:

```
sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui ros-humble-gazebo-ros-pkgs
```

## Setup

### Step 1 (workspace setup)

```
cd ~

mkdir -p piper_ws/src

cd piper_ws/src

git clone https://github.com/Dezinter8/piper_bot.git
```

### Step 2 (build)

```
cd ~/piper_ws

colcon build --symlink-install
```

### Step 3 - Run (Gazebo)

1'st terminal (Robot) - Simulation

```
cd ~/piper_ws

source install/setup.bash

ros2 launch piper_bot launch_sim.launch.py world:=./src/piper_bot/worlds/pipe.world
```

2'nd terminal (Robot/Dev) - Controlling robot movement

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

#### Moving the robot

To move the robot remember that the terminal window used for 2'nd comand has to be an active window.

Moving around:
u i o
j k l
m , .

#### Run (Production)

```
cd piper_ws/

source install/setup.bash

ros2 launch piper_bot rsp.launch.py
```

```
rviz2 -d src/piper_bot/config/view_bot.rviz
```

```
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```
