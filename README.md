# Bebop Bringup

This package contains the main launch file to bring up the Bebop drone system.

## Launch System

The launch system is orchestrated by the `start_bebop.sh` script, which uses `tmux` to create a new session with two panes:

*   **Top Pane:** Launches the Bebop autonomy container.
*   **Bottom Pane:** Launches the ROS 2 nodes, including the `ros1_cmd_vel_bridge` and `mjpeg_bridge`.

## Usage

To launch the system, run the following command:

```bash
bebop
```

This will create a new `tmux` session named `bebop` and attach to it. To detach from the session, press `Ctrl+b` then `d`. To re-attach, run `tmux attach -t bebop`.