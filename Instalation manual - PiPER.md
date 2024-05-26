# PiPER instalation manual

Here are the installation instructions for the physical layer of the project.

# Contents

- [Bot](#BOT)
  - [Ros installation](#Ros_BOT)
  - [Video node](#Video_BOT)
  - [Lidar node](#lidar_BOT)
  - [Pico motors node](#Pico_motors_BOT)
  - [Pico imu node](#Pico_imu_BOT)
  - [PiPER STARTUP SERVICE](#Startup_BOT)
- [Dev](#DEV)
  - [Ros installation](#Ros_DEV)
  - [Gui](#Gui_DEV)
  - [Camera](#Camera_DEV)
- [Project commands](#Project_commands)

## PART 1 - BOT {#BOT}

### Ros installation {#Ros_BOT}

1. Update your system

```
sudo apt update && sudo apt upgrade -y
```

2. Install necessary apps - GIT nano PYTHON PIP

```
sudo apt install git nano idle3 python3-pip -y
```

3. Check that 'UTF-8' is present in each entry

```
locale
```

4. Ensure that ubuntu universe repository is enabled

```
sudo apt install software-properties-common -y

sudo add-apt-repository universe
```

5. Add ros2 gpg key

```
sudo apt update && sudo apt install curl -y

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

6. Add repository to your source list

```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

7. Install ros 2 packages

```
sudo apt update && sudo apt upgrade -y

sudo apt install ros-humble-desktop -y

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

### Video node {#Video_BOT}

1. Install video for linux

```
sudo apt install v4l-utils -y

sudo apt install ros-${ROS_DISTRO}-v4l2-camera -y

sudo apt install ros-${ROS_DISTRO}-image-transport-plugins
```

2. Change resolution and video format

```
v4l2-ctl --device=/dev/video0 --set-fmt-video=width=640,height=480,pixelformat=YUYV
```

3. Git clone camera ctrl app and build

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

### Lidar node {#lidar_BOT}

1. Git clone lidar ros2 project

```
cd ~

mkdir -p ldlidar_ros2_ws/src

cd ldlidar_ros2_ws/src

git clone  https://github.com/ldrobotSensorTeam/ldlidar_sl_ros2.git

```

2. Change privlages on lidar connection

```
sudo chmod 777 /dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0
```

3. Find port_name and adjust it

Find in `ld14p.launch.py` port name `'port_name': '/dev/ttyUSB??'`
Replace current name with correct one

{'port_name': '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0'},

```
sudo nano ~/ldlidar_ros2_ws/src/ldlidar_sl_ros2/launch/ld14p.launch.py
```

4. Build lidar ros2 project

```
cd ~/ldlidar_ros2_ws

colcon build
```

### Pico motors node {#Pico_motors_BOT}

1. Install micro-ros agent

```
sudo snap install micro-ros-agent

sudo snap set core experimental.hotplug=true

sudo systemctl restart snapd
```

2. Pico testing

```
snap interface serial-port
```

3. Creating connection with pico

```
snap connect micro-ros-agent:serial-port snapd:pico
```

4. Launching micro ros

```
micro-ros-agent serial --dev /dev/serial/by-id/usb-Raspberry_Pi_Pico_E6614103E7114938-if00 baudrate=115200
```

### Pico imu node {#Pico_imu_BOT}

1. Installation:

```
cd ~/piperws/src

git clone https://github.com/Dezinter8/pico_connection.git

cd ../

colcon build --symlink-install
```

2. Granting permissions to the serial port:

```
sudo chmod 777 /dev/serial/by-id/usb-Raspberry_Pi_Pico_E660D4A0A772982F-if00
```

3. Project launch

```
cd ~/piperws

source install/setup.bash

ros2 run pico_connection serial_publisher
```

### PiPER STARTUP SERVICE {#Startup_BOT}

Disable all nodes created earlier

1. Create a service file

```
sudo nano /etc/systemd/system/ros2_launch.service
```

2. Paste the following into file `ros2_launch.service`

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

- This command performs a reload of the systemd configuration, which is needed after adding a new service file.

```
sudo systemctl enable ros2_launch.service
```

- This command enables the ros2_launch service so that it starts automatically when the system boots.

```
sudo systemctl start ros2_launch.service
```

- This command immediately starts the ros2_launch service, without rebooting the system.

```
journalctl -u ros2_launch.service
```

- This command will display all entries related to the `ros2_launch.service` service.

4. Create a new rules file in /etc/udev/rules.d/ to grant permissions to serial ports automatically:

```
sudo nano /etc/udev/rules.d/99-usb-serial.rules
```

5. Add the following content, gives permissions to both pico and lidar:

```
SUBSYSTEM=="tty", ATTRS{serial}=="E660D4A0A772982F", MODE="0666"
SUBSYSTEM=="tty", ATTRS{serial}=="E6614103E7114938", MODE="0666"
SUBSYSTEM=="tty", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{serial}=="0001", MODE="0666", SYMLINK+="my_serial"
```

6. After creating the rules file, you need to load the new udev configuration and apply the changes:

```
sudo udevadm control --reload-rules && sudo udevadm trigger
```

## PART 2 - DEV {#DEV}

### Ros installation {#Ros_DEV}

1. Update your system

```
sudo apt update && sudo apt upgrade -y
```

2. Install necessary apps - GIT nano PYTHON PIP

```
sudo apt install git nano idle3 python3-pip -y
```

3. Check that 'UTF-8' is present in each entry

```
locale
```

4. Ensure that ubuntu universe repository is enabled

```
sudo apt install software-properties-common -y

sudo add-apt-repository universe
```

5. Add ros2 gpg key

```
sudo apt update && sudo apt install curl -y

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

6. Add repository to your source list

```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

7. Install ros 2 packages

```
sudo apt update && sudo apt upgrade -y

sudo apt install ros-humble-desktop -y

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

### Gui {#Gui_DEV}

1. Git clone project gui

```
cd ~

git clone https://github.com/Dezinter8/Piper_Gui
```

2. Create python virtual env

```
sudo apt update && sudo apt install python3-virtualenv -y

cd ~/Piper_Gui

virtualenv venv

source venv/bin/activate

pip install PyQt5 vtk opencv-python-headless
```

### Camera {#Camera_DEV}

1. Install camera packages

```
sudo apt install ros-${ROS_DISTRO}-rqt-image-view -y

sudo apt install ros-${ROS_DISTRO}-image-transport-plugins
```

## PART 3 -- Project commands (Not necessary) {#Project_commands}

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

micro-ros-agent serial --dev /dev/serial/by-id/usb-Raspberry_Pi_Pico_E6614103E7114938-if00 baudrate=115200
```

After running the command, it is necessary to unplug and plug PICO again.

3. Run gui application - DEV

```
cd ~/piper_dev/Piper_Gui

source venv/bin/activate

python3 main.py
```

4. Controll robot movement from simulation- BOT / DEV

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
```
