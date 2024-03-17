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

git clone https://github.com/Dezinter8/Piper-bot-emulator.git
```

### Step 2 (build)

```
cd ~/piper_ws

colcon build --symlink-install

source install/setup.bash
```

### Step 3 (run)

1'st terminal (Robot)

```
cd ~/piper_ws

ros2 launch piper_bot launch_sim.launch.py world:=./src/piper_bot/worlds/obstacles.world
```

2'nd terminal (Robot)

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

3'rd terminal (best to lauch on dev machine. Can be done on Robot)

```
rviz2 -d ~/piper_ws/src/piper_bot/config/drive_bot.rviz
```

#### Splitting machines (Dev and robot)

To lauch Rviz on dev machine you might need to redo the whole process. All you need is drive_bot.rviz file, so you can copy it to dev home directory and specify file path in 3'rd comand like so.

```
rviz2 -d ~/drive_bot.rviz
```

#### Moving the robot

To move the robot remember that the terminal window used for 2'nd comand has to be an active window.

### Gazebo error

If gazebo is bricked try those comands:

```
pstree
```

```
killall -9 gzserver gzclient
```
