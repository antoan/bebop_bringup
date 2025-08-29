import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    """
    Launch file to bring up the Bebop drone system.
    """

    # Path to the shared_ros2 workspace
    shared_ros2_ws_path = os.path.expanduser('~/dev/robotics/shared_ros2')
    ros1_cmd_vel_bridge_pkg = os.path.join(shared_ros2_ws_path, 'src', 'ros1_cmd_vel_bridge')

    # Launch the ros1_cmd_vel_bridge forwarder
    ros1_cmd_vel_bridge = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros1_cmd_vel_bridge_pkg, 'launch', 'cmd_vel_forwarder.launch.py')
        ),
        launch_arguments={'ros1_host': 'localhost'}.items()
    )

    # Run the mjpeg_bridge from bebop_image_bridge
    mjpeg_bridge = ExecuteProcess(
        cmd=['ros2', 'run', 'bebop_image_bridge', 'mjpeg_bridge'],
        output='screen'
    )

    return LaunchDescription([
        ros1_cmd_vel_bridge,
        mjpeg_bridge,
    ])