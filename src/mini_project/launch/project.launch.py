from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='battery_temp_monitor',
            executable='listener',
            output='screen',
            prefix="gnome-terminal --"
            ),
        Node(
            package='battery_temp_monitor',
            executable='talker',
            output='screen', 
            prefix="gnome-terminal --"
            )
    ])