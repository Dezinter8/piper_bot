from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'launch', 'ldlidar_sl_ros2', 'ld14p.launch.py'],
            name='ldlidar',
        )
    ])

# Uruchomienie
# ros2 launch path/to/your/launch/file/LidarNode.py
