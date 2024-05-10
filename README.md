ROS2 

* UPDATE
```
    sudo apt update && sudo apt upgrade -y
```

* INSTALL NECESSARY APPS - GIT vsCODE PYTHON PIP
```
	sudo apt install git idle3 python3-pip -y

	sudo snap install code -y 
```

* CHECK FOR UTF-8
```
    locale
```

* FIRST ENSURE THAT UBUNTU UNIVERSE REPOSITORY IS ENABLED
```
    sudo apt install software-properties-common -y

    sudo add-apt-repository universe
```

* ADD ROS 2 GPG KEY
```
    sudo apt update && sudo apt install curl -y

    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

* ADD REPOSITORY TO YOUR SOURCE LIST
```
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

* INSTALL ROS 2 PACKAGES
```
    sudo apt update && sudo apt upgrade -y

    sudo apt install ros-humble-desktop -y

	sudo apt install python3-colcon-common-extensions -y
```

Environment setup 

* UPDATE
```
    sudo apt update && sudo apt upgrade -y
```

* INSTALL ROS PACKAGES
```
	sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui ros-humble-gazebo-ros-pkgs -y

	sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control -y
```

* ADD SOURCE TO YOUR BASHRC
```
	 echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

   	 source /opt/ros/humble/setup.bash

   	 ros2
```

* INSTALL VIDEO FOR LINUX
```
	sudo apt install v4l-utils -y
```

* CHECK V4L COMPLIANCE
```
	v4l2-compliance
```

* CHECK VIDEO FORMATS OF YOUR CAMERA
```
	v4l2-ctl --list-formats-ext --device /dev/video0
```

* OPTIONAL - CHANGE RESOLUTION AND VIDEO FORMAT
```
	v4l2-ctl --device=/dev/video0 --set-fmt-video=width=640,height=480,pixelformat=YUYV
```

* INSTALL ROS CAMERA V4L PACKAGES
```
	sudo apt install ros-${ROS_DISTRO}-v4l2-camera -y

	sudo apt install ros-${ROS_DISTRO}-image-transport-plugins
```

* GIT CLONE PROJECT BOT AND BUILD
```
   	cd ~

   	mkdir -p piper_ws/src

   	cd piper_ws/src

   	git clone https://github.com/Dezinter8/piper_bot.git

   	 cd ~/piper_ws

   	 colcon build --symlink-install
```

* GIT CLONE CAMERA CTRL APP AND BUILD
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

	 
Project commands


* Run simulation (Gazebo) - BOT 
```
   	cd ~/piper_ws

   	source install/setup.bash

   	ros2 launch piper_bot launch_sim.launch.py world:=./src/piper_bot/worlds/pipe.world
```

* Run gui application - DEV 
```
   	 cd ~/piper_dev/Piper_Gui

	 source venv/bin/activate

	python3 main.py
```

* Controll robot movement - BOT / DEV 
```
   	 ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
```

* Running camera node - BOT 
```
	ros2 run v4l2_camera v4l2_camera_node
```

* Reciving and displaying photos - DEV
```
	ros2 run rqt_image_view rqt_image_view
```

* Display ros2 nodes - BOT / DEV
```
	ros2 node list
```

* Display ros2 topic list  - BOT / DEV
```
	ros2 topic list
```

* Display ros2 topic message - BOT / DEV
```
	ros2 topic echo <topic name>
```

* Display ros2 detailed topic info - BOT / DEV
```
	ros2 topic info <topic name>

	ros2 interface show <Type:>
```

QT Designer

* Converting ui file to python
```
	pyuic5 mainwindow.ui -o MainWindow.py
```

* Converting resources to python
```
	pyrcc5 resources.qrc -o resources_rc.py
```





