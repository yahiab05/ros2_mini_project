from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mini_project',
            executable='listener',
            output='screen',
            prefix="gnome-terminal --"
            ),
        Node(
            package='mini_project',
            executable='talker',
            output='screen', 
            prefix="gnome-terminal --"
            )
    ])