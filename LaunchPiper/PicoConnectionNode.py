from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'run', 'pico_connection', 'serial_publisher'],
            name='pico_connection',
        )
    ])

# Uruchomienie
# ros2 launch path/to/your/launch/file/PicoConnectionNode.py
