#!/bin/bash
echo "Starting Bebop drone system..."

# Create a new tmux session and split the window
tmux new-session -d -s bebop
tmux split-window -v

# Run the container in the top pane
tmux send-keys -t bebop:0.0 'cd ~/dev/robotics/bebop_autonomy_image && ./launch.sh' C-m

# Run the ROS 2 nodes in the bottom pane
tmux send-keys -t bebop:0.1 'sleep 10 && ros2 launch bebop_bringup bebop_bringup.launch.py' C-m

# Attach to the tmux session
tmux attach -t bebop