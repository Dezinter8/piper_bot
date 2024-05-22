# PiPER project instalation manual
Here are the installation instructions for the virtual layer of the project.

## Part 0 - VM's

Prepare two virtual machines based on Ubuntu 22.04 LTS.

Naming scheme:
1. ubuntu - DEV
2. ubuntu - BOT

Machine settings: 
1. 4096MB RAM
2. 2 CORES
3. 128MB VRAM
4. Lan - BRIDGED
3. USB - Controller USB.3


## PART 1 - VM1 (ubuntu - BOT)

1. Update your system

```
sudo apt update && sudo apt upgrade -y
```

2. Install necessary apps - GIT vscode PYTHON PIP

```
sudo apt install git idle3 python3-pip -y
```

```
sudo snap install code -y
```

3. Check that 'UTF-8' is present in each entry

```
locale
```

4. Ensure that ubuntu universe repository is enabled

```
sudo apt install software-properties-common -y
```

```
sudo add-apt-repository universe
```

5. Add ros2 gpg key

```
sudo apt update && sudo apt install curl -y
```

```
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

6. Add repository to your source list

```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

7. Install ros 2 packages

```
sudo apt update && sudo apt upgrade -y
```

```
sudo apt install ros-humble-desktop -y
```

```
sudo apt install python3-colcon-common-extensions -y
```

8. Update your system

```
sudo apt update && sudo apt upgrade -y
```

9. Install ros packages

```
sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui ros-humble-gazebo-ros-pkgs -y
```

```
sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control -y
```

10. Add source to your bashrc

```
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

source /opt/ros/humble/setup.bash

ros2
```

11. Install video for linux

```
sudo apt install v4l-utils -y
```

12. Check v4l compliance

```
v4l2-compliance
```

13. Check video formats of your camera

```
v4l2-ctl --list-formats-ext --device /dev/video0
```

14. Change resolution and video format

```
v4l2-ctl --device=/dev/video0 --set-fmt-video=width=640,height=480,pixelformat=YUYV
```

15. Install ros camera v4l packages

```
sudo apt install ros-${ROS_DISTRO}-v4l2-camera -y
```

```
sudo apt install ros-${ROS_DISTRO}-image-transport-plugins
```

16. Git clone project bot and build

```
cd ~

mkdir -p piper_ws/src

cd piper_ws/src

 git clone https://github.com/Dezinter8/piper_bot.git

cd ~/piper_ws

colcon build --symlink-install
```

17. Git clone camera ctrl app and build

```
cd ~

mkdir -p piper_bot_camera

cd piper_bot_camera

git clone --branch ${ROS_DISTRO} https://gitlab.com/boldhearts/ros2_v4l2_camera.git src/v4l2_camera

sudo apt install python3-rosdep2

rosdep update

rosdep install --from-paths src/v4l2_camera --ignore-src -r -y

colcon build
```



## PART 2 - VM2 (ubuntu - DEV)

1. Update your system

```
sudo apt update && sudo apt upgrade -y
```

2. Install necessary apps - GIT vscode PYTHON PIP

```
sudo apt install git idle3 python3-pip -y
```

```
sudo snap install code -y 
```

3. Check for utf-8

```
locale
```

4. First ensure that ubuntu universe repository is enabled

```
sudo apt install software-properties-common -y
```

```
sudo add-apt-repository universe
```

5. Add ros 2 gpg key

```
sudo apt update && sudo apt install curl -y
```

```
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

6. Add repository to your source list

```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

7. Install ros 2 packages

```
sudo apt update && sudo apt upgrade -y
```

```
sudo apt install ros-humble-desktop -y
```

```
sudo apt install python3-colcon-common-extensions -y
```

8. Update your system

```
sudo apt update && sudo apt upgrade -y
```

9. Add source to your bashrc

```
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

source /opt/ros/humble/setup.bash

ros2
```

10. Git clone project gui

```
cd ~

mkdir -p piper_dev

cd piper_dev

git clone https://github.com/Dezinter8/Piper_Gui
```

11. Create pythonirtual env

```
sudo apt update && sudo apt install  python3-virtualenv -y

cd ~/piper_dev/Piper_Gui

virtualenv venv
 
source venv/bin/activate

pip install PyQt5 PyQt5-tools vtk opencv-python-headless
```

12. Install camera packages

```
sudo apt install ros-${ROS_DISTRO}-rqt-image-view -y
```

```
sudo apt install ros-${ROS_DISTRO}-image-transport-plugins
```

* Before using the camera module in the application, remember to add it in the USB settings section, and to allocate the camera device to the machine in the window settings.



## PART 3 - Project commands

1. Run simulation (Gazebo) - BOT 
```
cd ~/piper_ws

source install/setup.bash

ros2 launch piper_bot launch_sim.launch.py world:=./src/piper_bot/worlds/pipe.world
```

2. Run gui application - DEV 
```
cd ~/piper_dev/Piper_Gui

source venv/bin/activate

python3 main.py
```

3. Controll robot movement - BOT / DEV 
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
```

4. Running camera node - BOT 
```
ros2 run v4l2_camera v4l2_camera_node
```

5. Reciving and displaying photos - DEV
```
ros2 run rqt_image_view rqt_image_view
```

6. Display ros2 nodes - BOT / DEV
```
ros2 node list
```

7. Display ros2 topic list  - BOT / DEV
```
ros2 topic list
```

8. Display ros2 topic message - BOT / DEV
```
ros2 topic echo <topic name>
```

9. Display ros2 detailed topic info - BOT / DEV
```
ros2 topic info <topic name>
```

```
ros2 interface show <Type:>
```

## QT Designer

1. Converting ui file to python
```
pyuic5 mainwindow.ui -o MainWindow.py
```

2. Converting resources to python
```
pyrcc5 resources.qrc -o resources_rc.py
```











