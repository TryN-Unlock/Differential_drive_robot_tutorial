import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, TimerAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    robot_dir = get_package_share_directory('waypoint_follower')

    declare_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='true')
    declare_param_file_arg = DeclareLaunchArgument('params_file', 
            default_value= os.path.join(robot_dir, 'params', 'drive_robot_navigaion.yaml') )
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

    planner_server_node = Node(
        package = 'nav2_planner',
        executable = 'planner_server',
        name = 'nav2_goal_planner',
        output = 'screen',
        parameters = [params_file]
    )

    controller_server_node = Node(
        package = 'nav2_controller',
        executable = 'controller_server',
        name = 'nav2_controller_server',
        output = 'screen',
        parameters = [params_file]
    )

    bt_node = Node(
        package = 'nav2_bt_navigator',
        executable = 'bt_navigator',
        name = 'bt_navigator',
        output = 'screen',
        parameters = [params_file]
    )

    behaviour_server_node = Node(
        package = 'nav2_behaviors',
        executable = 'behavior_server',
        name = 'nav2_behavior_server',
        output = 'screen',
        parameters = [params_file]
    )

    lifecycle_manager_node1 = Node(
        package = 'nav2_lifecycle_manager',
        executable = 'lifecycle_manager',
        name = 'localization_lifecycle_manager',
        output = 'screen',
        parameters = [params_file]
    )

    lifecycle_manager_node3 = Node(
        package = 'nav2_lifecycle_manager',
        executable = 'lifecycle_manager',
        name = 'planner_lifecycle_manager',
        output = 'screen',
        parameters = [params_file]
    )

    navigation_node_group = GroupAction([
        map_server_node,
        amcl_node,
        lifecycle_manager_node1
    ])

    planner_node_group = GroupAction([
        planner_server_node,
        controller_server_node,
        behaviour_server_node,
        bt_node,
        lifecycle_manager_node3
    ])

    delayed_navigation = TimerAction(
        period = 1.0,
        actions = [navigation_node_group]
    )

    delayed_planner_controller = TimerAction(
        period = 2.0,
        actions = [planner_node_group]
    )

    ld.add_action(declare_sim_time_arg)
    ld.add_action(declare_param_file_arg)
    ld.add_action(declare_map_arg)
    ld.add_action(delayed_navigation)
    ld.add_action(delayed_planner_controller)
    return ld