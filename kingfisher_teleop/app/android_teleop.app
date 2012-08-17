display: Android Teleop
description: Drive a Kingfisher from Android with a touch joystick and video feed.
platform: kingfisher 
launch: kingfisher_teleop/android_teleop.launch
interface: kingfisher_teleop/android_teleop.interface
icon: kingfisher_teleop/android-lightning-turtlebot.png
clients:
 - type: android
   manager:
     api-level: 9
     intent-action: ros.android.teleop.Teleop
   app: 
     gravityMode: 0
     base_control_topic: /cmd_vel
     camera_topic: /camera/image_color/compressed_throttle
