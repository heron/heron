cmake_minimum_required(VERSION 2.8.3)
project(kingfisher_teleop)

find_package(catkin REQUIRED)

catkin_package()

install(PROGRAMS nodes/joystick_teleop
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
