# Piper real robot

![Piper](./src/piper.png)

# Piper simulation

![Piper](./src/piper_simulation.png)

## Pre requirements

- xacro
- joint-state-publisher
- gazebo

Install those using:

```
sudo apt-get update

sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui ros-humble-gazebo-ros-pkgs

sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control
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
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
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

### Robot doesn't spawn

After launching gazebo simulation with pipe model inside, don't close the gazebo window. Create new terminal and spawn robot manualy using this command:

```
ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity bit_name
```

## Data coming out from robot

### Wheels movement

```
ros2 topic echo /joint_states
```

position refers to wheel spins in radians, so how many times wheel make 360 from start.
velocity refers to wheels rotation speed.

You can also use this comand to see ros2_control interfaces for wheels:

```
ros2 control list_hardware_interfaces
```

### Accelerometer and gyroscope

To view data from accelerometer and gyroscope use this comand:

```
ros2 topic echo /imu_plugin/out
```

linear_acceleration refers to accelerometer data.
angular_velocity refers to gyroscope data.
