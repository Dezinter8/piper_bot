from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ldlidar_sl_ros2',
            executable='ld14p',
            name='ld14p_node',
        )
    ])
    
# Uruchomienie
# ros2 launch path/to/your/launch/file/LidarNode.py
