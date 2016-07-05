cmake_minimum_required(VERSION 2.8.3)
project(heron_msgs)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  Course.msg
  Drive.msg
  Helm.msg
  Sense.msg
  Status.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(CATKIN_DEPENDS std_msgs message_runtime)
