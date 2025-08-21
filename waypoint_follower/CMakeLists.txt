cmake_minimum_required(VERSION 3.8)
project(waypoint_follower)

find_package(gz-transport13 QUIET REQUIRED OPTIONAL_COMPONENTS log)
set(GZ_TRANSPORT_VER ${gz-transport13_VERSION_MAJOR})

include_directories(${CMAKE_BINARY_DIR})

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(slam_toolbox REQUIRED)
find_package(nav2_lifecycle_manager REQUIRED)
find_package(nav2_map_server REQUIRED)
find_package(nav2_amcl REQUIRED)
find_package(nav2_bringup REQUIRED)
find_package(nav2_costmap_2d REQUIRED)

install(
  DIRECTORY model launch rviz params worlds maps
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
