#!/usr/bin/python

import roslib; roslib.load_manifest('kingfisher_teleop')
import rospy

from sensor_msgs.msg import Joy,Imu
from geometry_msgs.msg import Twist,Wrench
from kingfisher_msgs.msg import YawSpd, Helm
from tf.transformations import euler_from_quaternion


class Teleop:
    def __init__(self):
        rospy.init_node('clearpath_teleop')

        self.rotation_scale = rospy.get_param('~rotation_scale',0.5) #rad/s
        self.fwd_vel_scale = rospy.get_param('~fwd_vel_scale', 5) #m/s
        self.bck_vel_scale = rospy.get_param('~bck_vel_scale',0.5) #m/s

        self.boat_width = 0.381
        self.fwd_force_scale = rospy.get_param('~fwd_force_scale',75) #Newtons
        self.bck_force_scale = rospy.get_param('~bck_force_scale',40) #Newtons
        self.torque_scale = rospy.get_param('~torque_scale',self.bck_force_scale*2*self.boat_width) #N.m, max torque depends on max reverse thrust possible
         
        self.deadman_button = rospy.get_param('~deadman_button', 0)
        #self.turbo_button = rospy.get_param('~turbo_button', 1)
        self.heading_hold_button = rospy.get_param('~heading_hold_button',3)
        self.autonomous_button = rospy.get_param('~autonomous_button',2)

        self.autonomous = False
        self.last_auto_button = 0

        self.heading_hold = False
        self.curr_heading=0
        self.hold_heading = 0
        self.last_heading_button = 0

        self.max_age = None
        max_age_seconds = rospy.get_param('~max_age_seconds', None)
        if max_age_seconds:
            self.max_age = rospy.Duration.from_sec(max_age_seconds)

        self.helm_pub = rospy.Publisher('cmd_helm', Helm)
        self.wrench_pub = rospy.Publisher('cmd_wrench',Wrench)
        self.heading_pub = rospy.Publisher('cmd_yawspd',YawSpd)


        rospy.Subscriber("joy", Joy, self.callback)
        rospy.Subscriber("imu/data_final",Imu,self.imu_callback) 
        rospy.spin()
   
    def output_mode(self):
        if (self.heading_hold):
            rospy.loginfo("Boat under heading hold")
            self.hold_heading = self.curr_heading
        elif (self.autonomous):
            rospy.loginfo("Boat under helm control")
        else:
            rospy.loginfo("Boat in raw R/C mode")

    def imu_callback(self,data):
        q  = data.orientation
        x,y,z = euler_from_quaternion([ getattr(q,f) for f in q.__slots__])
        self.curr_heading = z
    
    def callback(self, data):
        """ Receive joystick data, formulate Twist message. """
        #print (data.header.stamp - rospy.Time.now()).to_sec() 
        if self.max_age and data.header.stamp - rospy.Time.now() > self.max_age:
            # Joystick messages are too delayed. Discard them.
            return
        
        auto_button = data.buttons[self.autonomous_button]
        heading_button = data.buttons[self.heading_hold_button]

        #catch button transition
        if heading_button==1 and self.last_heading_button==0:
            self.heading_hold=not self.heading_hold
            self.output_mode()
        elif auto_button==1 and self.last_auto_button==0:
            self.autonomous = not self.autonomous 
            self.output_mode()
        
        self.last_auto_button = auto_button
        self.last_heading_button = heading_button

        if (self.heading_hold):
            scale = 0
            if data.buttons[self.deadman_button] == 1:
                if (data.axes[1] >= 0):
                    scale = self.fwd_vel_scale 
                else:
                    scale = self.bck_vel_scale
                cmd=YawSpd()
                cmd.heading = self.hold_heading
                cmd.speed = data.axes[1] * scale
                self.heading_pub.publish(cmd)



        elif (self.autonomous): #command closed loop yaw rate + thrust pct on helm message
            if data.buttons[self.deadman_button] == 1:
                #if (data.axes[1] >= 0):
                #    scale = self.fwd_vel_scale 
                #else:
                #    scale = self.bck_vel_scale
                
                scale = 1
                cmd = Helm()
                cmd.yaw_rate = data.axes[0] * self.rotation_scale 
                cmd.thrust_pct = data.axes[1] * scale
                self.helm_pub.publish(cmd)
        else: # command open loop thrusters on a wrench message
            scale = 0
            if data.buttons[self.deadman_button] == 1:
                if (data.axes[1] >= 0):
                    scale = self.fwd_force_scale 
                else:
                    scale = self.bck_force_scale
                cmd = Wrench()
                cmd.torque.z = data.axes[0] * self.torque_scale
                cmd.force.x = data.axes[1]  * scale
                self.wrench_pub.publish(cmd)


if __name__ == "__main__": Teleop()
