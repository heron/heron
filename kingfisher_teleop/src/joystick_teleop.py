#!/usr/bin/python

import roslib; roslib.load_manifest('kingfisher_teleop')
import rospy

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist,Wrench


class Teleop:
    def __init__(self):
        rospy.init_node('clearpath_teleop')

        self.rotation_scale = rospy.get_param('~rotation_scale',0.5) #rad/s
        self.fwd_vel_scale = rospy.get_param('~fwd_vel_scale', 75) #m/s
        self.bck_vel_scale = rospy.get_param('~bck_vel_scale',40) #m/s

        self.boat_width = 0.381
        self.fwd_force_scale = rospy.get_param('~fwd_force_scale',75) #Newtons
        self.bck_force_scale = rospy.get_param('~bck_force_scale',40) #Newtons
        self.torque_scale = rospy.get_param('~torque_scale',self.bck_force_scale*2*self.boat_width) #N.m, max torque depends on max reverse thrust possible
         
        self.deadman_button = rospy.get_param('~deadman_button', 0)
        #self.turbo_button = rospy.get_param('~turbo_button', 1)
        self.closed_loop = rospy.get_param('~closed_loop',False)
        self.autonomous_button = rospy.get_param('~autonomous_button',2)

        self.autonomous = False
        self.last_auto_button = 0

        self.max_age = None
        max_age_seconds = rospy.get_param('~max_age_seconds', None)
        if max_age_seconds:
            self.max_age = rospy.Duration.from_sec(max_age_seconds)

        self.vel_pub = rospy.Publisher('cmd_vel', Twist)
        self.wrench_pub = rospy.Publisher('cmd_wrench',Wrench)

        rospy.Subscriber("joy", Joy, self.callback)
        rospy.spin()
    
    def callback(self, data):
        """ Receive joystick data, formulate Twist message. """
        #print (data.header.stamp - rospy.Time.now()).to_sec() 
        if self.max_age and data.header.stamp - rospy.Time.now() > self.max_age:
            # Joystick messages are too delayed. Discard them.
            return
        
        auto_button = data.buttons[self.autonomous_button]
        if auto_button==1 and self.last_auto_button==0: #catch button transition
            self.autonomous = not self.autonomous 
            if (self.autonomous):
                rospy.loginfo("Boat under closed loop control")
            else:
                rospy.loginfo("Boat in R/C mode")
        self.last_auto_button = auto_button

        if (self.autonomous): #command closed loop velocites on a twist message
            scale = 0
            if data.buttons[self.deadman_button] == 1:
                if (data.axes[1] >= 0):
                    scale = self.fwd_vel_scale 
                else:
                    scale = self.bck_vel_scale
                cmd = Twist()
                cmd.angular.z = -data.axes[0] * self.rotation_scale 
                cmd.linear.x = data.axes[1] * scale
                self.vel_pub.publish(cmd)

        else: # command open loop thrusters on a wrench message
            scale = 0
            if data.buttons[self.deadman_button] == 1:
                if (data.axes[1] >= 0):
                    scale = self.fwd_force_scale 
                else:
                    scale = self.bck_force_scale
                cmd = Wrench()
                cmd.torque.z = -data.axes[0] * self.torque_scale
                cmd.force.x = data.axes[1]  * scale
                self.wrench_pub.publish(cmd)


if __name__ == "__main__": Teleop()
