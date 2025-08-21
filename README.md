
# Differential Drive Robot Tutorial

A beginner's guide for new ROS2 and Gazebo Sim users to make and simulate their very first robot. This tutorial includes a series of singular projects from visualizing a basic robot structure to using the Nav2 Stack to allow the robot to move through a controlled environment in Gazebo Sim. 

## Prerequisties

1. ROS2 Jazzy 
2. Gazebo Sim (Harmonic)
3. Beginner's level understanding of ROS2 framework, i.e. Nodes, topics, interfaces, services, etc. For those who are a complete beginner, please refer to [ROS2 Beginner's Tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools.html).

## WalkThrough

The tutorial is meant to showcase to beginners; ROS2, Gazebo, Nav2 and RViz capabilities at a fundamental level and intends to help individuals like myself, to understand the flow of how to built the simulation of any robot and the necessary components to implement into it as well. The steps are as follows:

1. Visualzation of Robot: Rviz
    This part includes the forming of basic shapes for making the robot and visualizing the same in RViz2. The details for for that be found inside [drive_robot_visualization](https://github.com/TryN-Unlock/Differential_drive_robot_tutorial/blob/master/drive_robot_visualization/README.md) project.

2. Simulation on Gazebo
    This part includes the addition of the physical features of the robot based on its shape to simulate it on Gazebo Sim. The details for that be found inside [drive_robot_gazebo](https://github.com/TryN-Unlock/Differential_drive_robot_tutorial/blob/master/drive_robot_gazebo/README.md) project.

3. Creation of World and Teleoperation of Robot
    This part shows how to create a .sdf formatted world file and move the robot inside this world using basic controls. The details for that be found inside [gazebo_teleop_world](https://github.com/TryN-Unlock/Differential_drive_robot_tutorial/blob/master/gazebo_teleop_world/README.md) project.

4. Sensor Integration
    This part explains the use of each sensor for the robot and how visualize the data for these sensors inside Rviz. The details for that be found inside [sensors](https://github.com/TryN-Unlock/Differential_drive_robot_tutorial/blob/master/sensors/README.md) project.

5. Mapping of world using SLAM
    This part includes the SLAM Toolbox for mapping the made environment and saving as well. The details for that be found inside [mapping_slam](https://github.com/TryN-Unlock/Differential_drive_robot_tutorial/blob/master/mapping_slam/README.md) project.

6. Localization using AMCL
    This part address the inclusion of Extended Kalman Filter, simply called EKF and the use of AMCL. The details for that be found inside [localization_teleop](https://github.com/TryN-Unlock/Differential_drive_robot_tutorial/blob/master/localization_teleop/README.md) project.

7. Waypoint Follower 
    This is the final part and shows the use of Nav2 Stack to inplement a waypoint follower robot. The details for that be found inside [waypoint_follower](https://github.com/TryN-Unlock/Differential_drive_robot_tutorial/blob/master/waypoint_follower/README.md) project.

# Acknowledgement

This tutorial is made using a collection of resources from a number of people/organizations and I wish to mention them below:

1. The robot model was devised from the guidance of the following course, [ROS 2 for Beginners Level 2 - TF | URDF | RViz | Gazebo - Edouard Renard](https://www.udemy.com/course/ros2-tf-urdf-rviz-gazebo/)  
2. [Nav2 Stack](https://docs.nav2.org/index.html)
3. [SLAM Toolbox Github Page](https://github.com/SteveMacenski/slam_toolbox)

# Note

This is also my first ROS2-based project. Feedback would be appreciated.

## Contributions

For those who wish to contribute further to this project or have noticed or found any issue with the current setup of this project, please use the Issues resource available.