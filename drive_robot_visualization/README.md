
# Differential Drive Robot Visualziation on Rviz

This project showcases the modeling and shaping of the structure of the robot that one would like to make. The XML-based language format shows the structure to write basic shape that includes cuboid, sphere and cylinder which are combined to form a wheeled-robot. The size and proportion of the robot can be anything you desire.

## Note 

However, with coding; it must be taken into consideration that the scope of visualization is limited and for custom shapes and their visualization, CAD-based software must be used.

# Lesson

XML is a markup based language, which means that it utilises tag inside angle brackets to formalise a coded structure. Here are some fundamental tags to be known to start with:

| Tag  |Description|
|------------|------------------------------------------------------------------------------|
| `<robot>`| This tag holds on to the entire description of your robot. All other tags must come under this one. |
| `<link>` | Every physical and visible structure in the robot is called a link this is where that structure is described. |
| `<joint>`| Just like human anatomy, a structure that joins two links is a joint. |
| `<origin>`| This is holds the data of the position of the center of gravity of any link/joint. |
| `<axis>`| The axis about which a joint will rotate in 3-D geometry. |

## Understanding TF

TF in ROS2 pertains to Transform, which is a format of knowing how each link inside a robot is connected to another and using which joint. All this data about the connection of links and joints form what is commonly called as a TF tree. Note that, every robot will have only one "main" link that is formally called the root link of the robot, this link is essentially where the robot's entire structure originates from. There **MUST NOT BE** more than **ONE** root link. For a more in depth understanding of TF and TF tree, please refer the [ROS2 TF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html) guide.

# Prerequisites

Before running the project, please ensure that you have ROS2 and Rviz2 installed on your system. To verify ROS2 enter the following command on your terminal: 
`echo $ROS_DISTRO`
and to install/check Rviz2, enter this:
`sudo apt install ros-[ROS2_DISTRO]-rviz2`
This will install rviz2 on your system, just replace \[ROS2_DISTRO\] with the ROS2 distribution on your system.

# Running the simulation

With Prerequisites satisfied, run the following command on your terminal to visualize the robot. First, we move to the place where you have downloaded the project package:
`cd path/to/project_directory`

Then we build the package:
`colcon build --packages-select drive_robot_visualization`

\* Use Tab key for autocompletion.

Now we source the overlay of the current workspace setup:
`source install/setup.bash`

Finally we launch the project:
`ros2 launch drive_robot_visualization project.launch.xml`

Do play around with the numbers/values to see how the shape of the robot changes and follow step 2-4 in running the simulation to see the changes. I encourage you to actually type out a second file to better practise and visualize your own robot.