

Virtual Navigation Path Introduction:
Using lines drawn on the actual ground for robot navigation is limited by lighting conditions and is not conducive to optimal path planning. Designing navigation paths in the grid maps used by robots in SLAM (Simultaneous Localization and Mapping) can avoid the drawbacks of real-world line navigation.

Software Architecture:
This project is developed on the basis of the Zhongde xbot-u intelligent robot. The source code for the Zhongde robot can be found at the provided link.
https://github.com/DroidAITech/xbot_navi
Installation Tutorial:
On the basis of the project, copy the entire \xbot\xbot_navi folder from this project into the \xbot folder of the project.

Usage Instructions:
If you want to use virtual obstacles to construct the robot's activity space for navigation, follow these steps:

1. Launch command: roslaunch xbot_navi xbot_virnav.launch
2. Launch command: roslaunch xbot_navi view_rviz.launch

If you want to use virtual path points for navigation, after starting the robot, run the following commands:

1. Launch command: roslaunch xbot_navi build_map.launch
2. Run command: rosrun xbot_navi zhouxbot_getpositon.py to record the points the robot needs to travel
3. Place the robot back at the starting point recorded earlier
4. Run command: rosrun xbot_navi zhouxbot_publish_virnav.py
The robot will then navigate according to the trajectory stored in the previous step.
