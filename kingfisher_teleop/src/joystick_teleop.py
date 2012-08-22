#!/usr/bin/python

import roslib; roslib.load_manifest('kingfisher_teleop')
import rospy

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class Teleop:
    def __init__(self):
        rospy.init_node('clearpath_teleop')

        self.turn_scale = rospy.get_param('~turn_scale')
        self.drive_scale = rospy.get_param('~drive_scale')
        self.deadman_button = rospy.get_param('~deadman_button', 0)

        self.cmd_pub = rospy.Publisher('cmd_vel', Twist)

        rospy.Subscriber("joy", Joy, self.callback)
        rospy.spin()
    
    def callback(self, data):
        """ Receive joystick data, formulate Twist message. """
        if data.buttons[self.deadman_button] == 1:
            cmd = Twist()
            cmd.linear.x = data.axes[1] * self.drive_scale
            cmd.angular.z = data.axes[0] * self.turn_scale
            self.cmd_pub.publish(cmd)


if __name__ == "__main__": Teleop()
