#!/usr/bin/python

import roslib; roslib.load_manifest('kingfisher_teleop')
import rospy

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class Teleop:
    def __init__(self):
        rospy.init_node('clearpath_teleop')

        self.turn_scale = rospy.get_param('~turn_scale')
        self.drive_scale = rospy.get_param('~drive_scale', 0.7)
        self.turbo_drive_scale = rospy.get_param('~turbo_drive_scale', 1.0)

        self.deadman_button = rospy.get_param('~deadman_button', 0)
        self.turbo_button = rospy.get_param('~turbo_button', 1)

        self.max_age = None
        max_age_seconds = rospy.get_param('~max_age_seconds', None)
        if max_age_seconds:
            self.max_age = rospy.Duration.from_sec(max_age_seconds)

        self.cmd_pub = rospy.Publisher('cmd_vel', Twist)

        rospy.Subscriber("joy", Joy, self.callback)
        rospy.spin()
    
    def callback(self, data):
        """ Receive joystick data, formulate Twist message. """
        #print (data.header.stamp - rospy.Time.now()).to_sec() 
        if self.max_age and data.header.stamp - rospy.Time.now() > self.max_age:
            # Joystick messages are too delayed. Discard them.
            return

        scale = 0
        if data.buttons[self.deadman_button] == 1:
            scale = self.drive_scale
        if data.buttons[self.turbo_button] == 1:
            scale = self.turbo_drive_scale

        if scale != 0:
            cmd = Twist()
            cmd.linear.x = data.axes[1] * scale
            cmd.angular.z = data.axes[0] * self.turn_scale
            self.cmd_pub.publish(cmd)


if __name__ == "__main__": Teleop()
