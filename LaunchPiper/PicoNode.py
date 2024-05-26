from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['micro-ros-agent', 'serial', '--dev', '/dev/serial/by-id/usb-Raspberry_Pi_Pico_E6614103E7114938-if00', 'baudrate=115200'],
            name='micro_ros_agent',
        )
    ])
    
# Uruchomienie
# ros2 launch path/to/your/launch/file/PicoNode.py
