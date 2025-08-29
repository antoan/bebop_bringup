import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess

def generate_launch_description():
    """
    Launch file to bring up the Bebop autonomy container.
    """

    # Path to the bebop_autonomy_image workspace
    bebop_autonomy_ws_path = os.path.expanduser('~/dev/robotics/bebop_autonomy_image')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['./launch_container.sh'],
            cwd=os.path.join(get_package_share_directory('bebop_bringup'), 'scripts'),
            shell=True,
            output='screen'
        )
    ])