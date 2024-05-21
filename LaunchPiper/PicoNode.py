from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['micro-ros-agent', 'serial', '--dev', '/dev/ttyACM0', 'baudrate=115200'],
            name='micro_ros_agent',
            output='screen'
        )
    ])
    
# Uruchomienie
# ros2 launch path/to/your/launch/file/PicoNode.py
