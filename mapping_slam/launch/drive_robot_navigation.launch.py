import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, TimerAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, LifecycleNode

def generate_launch_description():
    ld = LaunchDescription()

    robot_dir = get_package_share_directory('ros2_udemy_project_pkg')

    declare_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='true')
    declare_param_file_arg = DeclareLaunchArgument('params_file', 
            default_value= os.path.join(robot_dir, 'params', 'drive_robot_navigation.yaml') )

    use_sim_time = LaunchConfiguration('use_sim_time')
    params_file = LaunchConfiguration('params_file')

    slam_toolbox_node = LifecycleNode(
        package = 'slam_toolbox',
        executable = 'async_slam_toolbox_node',
        name = 'slam_toolbox',
        output = 'screen',
        parameters = [params_file,
                    {'use_sim_time': use_sim_time}
        ],
        namespace = ''
    )

    lifecycle_manager_node1 = Node(
        package = 'nav2_lifecycle_manager',
        executable = 'lifecycle_manager',
        name = 'localization_lifecycle_manager',
        output = 'screen',
        parameters = [params_file]
    )

    navigation_node_group = GroupAction([
        slam_toolbox_node,
        lifecycle_manager_node1
    ])

    delayed_navigation = TimerAction(
        period = 1.0,
        actions = [navigation_node_group]
    )

    ld.add_action(declare_sim_time_arg)
    ld.add_action(declare_param_file_arg)
    ld.add_action(delayed_navigation)
    return ld