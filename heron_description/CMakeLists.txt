cmake_minimum_required(VERSION 2.8.3)
project(heron_description)

find_package(catkin REQUIRED COMPONENTS
    heron_msgs
    uuv_gazebo_ros_plugins_msgs
)

catkin_package(
  CATKIN_DEPENDS heron_msgs uuv_gazebo_ros_plugins_msgs
)

roslaunch_add_file_check(launch/description.launch)

install(DIRECTORY meshes launch urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS scripts/env_run
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
