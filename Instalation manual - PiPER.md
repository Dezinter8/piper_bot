
# PiPER instalation manual

Here are the installation instructions for the physical layer of the project.

## PART 1 - BOT

1. Update your system

```
sudo apt update && sudo apt upgrade -y
```

2. Install necessary apps - GIT nano vscode PYTHON PIP

```
sudo apt install git nano idle3 python3-pip -y
```

```
sudo snap install code --classic
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

9. Add source to your bashrc

```
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

source /opt/ros/humble/setup.bash

ros2
```

10. Install video for linux

```
sudo apt install v4l-utils -y
```

11. Change resolution and video format

```
v4l2-ctl --device=/dev/video0 --set-fmt-video=width=640,height=480,pixelformat=YUYV
```

12. Install ros camera v4l packages

```
sudo apt install ros-${ROS_DISTRO}-v4l2-camera -y
```

```
sudo apt install ros-${ROS_DISTRO}-image-transport-plugins
```


13. Git clone camera ctrl app and build

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

14. Git clone lidar ros2 project

```
cd ~

mkdir -p ldlidar_ws/src

cd ldlidar_ws/src

sudo git clone  https://github.com/ldrobotSensorTeam/ldlidar_sl_ros2.git

```


15. Change privlages on lidar connection 

```
ls /dev/ttyUSB*
```

```
cd ~/ldlidar_ros2_ws

sudo chmod 777 /dev/ttyUSB0
```

16. Find port_name and adjust it

Find in `ld14p.launch.py` port name ` 'port_name': '/dev/ttyUSB??' `
Replace current name with correct one (name schould be find using command ` ls /dev/ttyUSB* ` )

```
ls /dev/ttyUSB* 
```
``` 
sudo nano ~/ldlidar_ws/src/ldlidar_sl_ros2/launch/ld14p.launch.py 
```

17. Build lidar ros2 project

```
cd ~/ldlidar_ws

colcon build
```


18. Install necessary micro ros packages

```
sudo apt install build-essential cmake gcc-arm-none-eabi libnewlib-arm-none-eabi doxygen python3
```

19. Create pico workspace

```
cd ~

mkdir pico

cd pico
```


20. Git clone micro ros repo's

```
git clone --recurse-submodules https://github.com/raspberrypi/pico-sdk.git
```

```
git clone https://github.com/micro-ROS/micro_ros_raspberrypi_pico_sdk.git
```

21. Using vscode prepare workspace

```
cd ~/pico/micro_ros_raspberrypi_pico_sdk

mkdir .vscode

touch .vscode/settings.json
```


22. Set up .json file in correct way

Add to .json file in .vscode directory

```
nano .vscode/settings.json
```

This lines of code

```
{
    "cmake.configureEnvironment": {
        "PICO_SDK_PATH": "/home/bot/pico/pico-sdk",
    },
}
```

23. Build project using vscode

```
cd ~/pico/micro_ros_raspberrypi_pico_sdk

code .
```

Choose `gcc-arm-none-eabi`

If there is no message use this `Ctr + Shift + p` and choose `CMake: Build` option. Your project schould build itself.

24.	Install micro-ros agent

```
sudo snap install micro-ros-agent

sudo snap set core experimental.hotplug=true

sudo systemctl restart snapd
```


25. Flashing raspberry pico

Check for .uf2 file in `micro_ros_raspberrypi_pico_sdk/build` directory. If it doesn't exist build procedure wasn't succesful.

```
cd ~/pico/micro_ros_raspberrypi_pico_sdk/build

ls
```

Connect PICO to your computer while holding down the `BOOTSEL` button, when it detects the PICO, copy the `.uf2` file there. There will be an automatic restart of the PICO. 

26. Pico testing

```
snap interface serial-port
```

27. Creating connection with pico 

```
snap connect micro-ros-agent:serial-port snapd:pico
```
### PiPER STARTUP SERVICE

1. Create a service file
```
sudo nano /etc/systemd/system/ros2_launch.service
```

2. File `ros2_launch.service`

```
[Unit]
Description=Uruchamia skrypt ROS 2 launch przy starcie systemu

[Service]
Type=simple
ExecStart=/bin/bash -c '. /opt/ros/humble/setup.bash; ros2 launch /home/bot/piper_ws/src/piper_bot/LaunchPiper/MasterLaunch.py'


[Install]
WantedBy=multi-user.target
```

This file contains the definition of the service that runs the ROS 2 launch MasterLaunch.py script after system startup. Make sure the paths are correct and match your configuration.

3. Enabling the startup service for PiPER

```
sudo systemctl daemon-reload
```
* This command performs a reload of the systemd configuration, which is needed after adding a new service file.

```
sudo systemctl enable ros2_launch.service
```
* This command enables the ros2_launch service so that it starts automatically when the system boots.

```
sudo systemctl start ros2_launch.service
```
* This command immediately starts the ros2_launch service, without rebooting the system.
```
journalctl -u ros2_launch.service
```
* This command will display all entries related to the `ros2_launch.service` service.

## PART 2 - DEV

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

11. Create python virtual env

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


## PART 3 -- Project commands

1. Start camera node - BOT 

```
source .bashrc

ros2 run v4l2_camera v4l2_camera_node
```


2. Start lidar node - BOT

```
cd ~/ldlidar_ros2_ws

source install/local_setup.bash

ros2 launch ldlidar_sl_ros2 ld14p.launch.py
```

3. Start pico node - BOT


```
source .bashrc

micro-ros-agent serial --dev /dev/ttyACM0 baudrate=115200
```
### After running the command, it is necessary to unplug and plug PICO again.

3. Run gui application - DEV 
```
cd ~/piper_dev/Piper_Gui

source .bashrc

source venv/bin/activate

ros2 run rqt_image_view rqt_image_view

python3 main.py
```


4. Controll robot movement - BOT / DEV 
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
```


5. Display ros2 nodes - BOT / DEV
```
ros2 node list
```

6. Display ros2 topic list  - BOT / DEV
```
ros2 topic list
```

7. Display ros2 topic message - BOT / DEV
```
ros2 topic echo <topic name>
```

8. Display ros2 detailed topic info - BOT / DEV

```
ros2 topic info <topic name>
```
```
ros2 interface show <Type:>
```




