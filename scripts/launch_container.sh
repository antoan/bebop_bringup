#!/bin/bash
tmux kill-session -t bebop 2>/dev/null || true
cd ~/dev/robotics/bebop_autonomy_image && tmux new-session -d -s bebop './launch.sh'