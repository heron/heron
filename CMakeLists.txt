cmake_minimum_required(VERSION 2.8.3)
project(kingfisher_msgs)

find_package(catkin REQUIRED message_generation)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  Sense.msg
  Drive.msg
)

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

generate_messages()

catkin_package()

