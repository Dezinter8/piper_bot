import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():
    # Set the package name for the robot_state_publisher launch file
    package_name = 'piper_bot'  # <-- Make sure this is correct for your setup

    # Include the robot_state_publisher launch file, make sure simulation time is enabled
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file from the gazebo_ros package
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')])
    )

    # Define the spawn_entity node action from the gazebo_ros package
    spawn_entity = Node(
        package='gazebo_ros', 
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'my_bot'],
        output='screen'
    )

    # Delay the spawn_entity action by 1 second using TimerAction
    delayed_spawn_entity = TimerAction(
        period=1.0,  # Delay period in seconds
        actions=[spawn_entity]
    )

    # Launch the robot_state_publisher, Gazebo, and the delayed spawn_entity
    return LaunchDescription([
        rsp,
        gazebo,
        delayed_spawn_entity,
    ])
