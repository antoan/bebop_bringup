# Bebop Bringup

This package contains the main launch file to bring up the Bebop drone system.

## Launch System

The launch system is designed to address the challenge of launching a non-ROS Docker container alongside ROS 2 nodes. The ROS 2 launch system is primarily designed for ROS nodes, and it does not provide a reliable way to manage the lifecycle of a long-running, non-ROS process like a Docker container.

To overcome this limitation, we use a custom shell script, `start_bebop.sh`, as the main entry point for launching the system. This script provides the necessary orchestration to ensure that both the Docker container and the ROS 2 nodes are launched correctly.

The `start_bebop.sh` script uses `tmux`, a terminal multiplexer, to create a new session with two separate panes. This approach provides several advantages:

*   **Isolation:** The Docker container and ROS 2 nodes run in separate terminal panes, preventing them from interfering with each other.
*   **Lifecycle Management:** The `start_bebop.sh` script manages the lifecycle of both the container and the ROS 2 nodes, ensuring they are started in the correct order.
*   **Debugging:** The separate panes make it easier to debug issues with either the container or the ROS 2 nodes.

The launch sequence is as follows:

1.  The `bebop` alias executes the `start_bebop.sh` script.
2.  The `start_bebop.sh` script creates a new `tmux` session named `bebop`.
3.  The `tmux` window is split into two panes.
4.  The top pane launches the Bebop autonomy container.
5.  The bottom pane waits for 10 seconds to allow the container to start, and then launches the ROS 2 nodes, including the `ros1_cmd_vel_bridge` and `mjpeg_bridge`.

## Usage

To launch the system, run the following command:

```bash
bebop
```

This will create a new `tmux` session named `bebop` and attach to it. To detach from the session, press `Ctrl+b` then `d`. To re-attach, run `tmux attach -t bebop`.