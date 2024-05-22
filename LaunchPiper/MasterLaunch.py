from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.realpath(__file__))

    return LaunchDescription([
        TimerAction(
            period=10.0,  # 10-second delay
            actions=[
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(os.path.join(current_dir, 'CameraNode.py'))
                ),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(os.path.join(current_dir, 'PicoNode.py'))
                ),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(os.path.join(current_dir, 'LidarNode.py'))
                ),
            ]
        )
    ])
    
# Uruchomienie
# ros2 launch path/to/your/launch/file/MasterLaunch.py)
