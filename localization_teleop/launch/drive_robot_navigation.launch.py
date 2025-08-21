import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, TimerAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    robot_dir = get_package_share_directory('localization_teleop')

    declare_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='true')
    declare_param_file_arg = DeclareLaunchArgument('params_file', 
            default_value= os.path.join(robot_dir, 'params', 'nav2_amcl.yaml') )
    declare_map_arg = DeclareLaunchArgument('map', 
            default_value= os.path.join(robot_dir, 'maps', 'map_1749722252.yaml') )

    use_sim_time = LaunchConfiguration('use_sim_time')
    params_file = LaunchConfiguration('params_file')
    map_file = LaunchConfiguration('map')

    map_server_node = Node(
        package = 'nav2_map_server',
        executable = 'map_server',
        name = 'map_server',
        output = 'screen',
        parameters = [
            params_file,
            {'yaml_filename': map_file},
            {'use_sim_time': use_sim_time}
        ],
    )

    amcl_node = Node(
        package = 'nav2_amcl',
        executable = 'amcl',
        name = 'amcl',
        output = 'screen',
        parameters = [params_file],
    )

    lifecycle_manager_node1 = Node(
        package = 'nav2_lifecycle_manager',
        executable = 'lifecycle_manager',
        name = 'localization_lifecycle_manager',
        output = 'screen',
        parameters = [params_file]
    )

    navigation_node_group = GroupAction([
        map_server_node,
        amcl_node,
        lifecycle_manager_node1
    ])

    delayed_navigation = TimerAction(
        period = 1.0,
        actions = [navigation_node_group]
    )

    ld.add_action(declare_sim_time_arg)
    ld.add_action(declare_param_file_arg)
    ld.add_action(declare_map_arg)
    ld.add_action(delayed_navigation)
    return ld