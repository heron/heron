#!/usr/bin/env python
# Software License Agreement (BSD)
#
# @author    Guy Stoppi <gstoppi@clearpathrobotics.com>
# @copyright (c) 2018, Clearpath Robotics, Inc., All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that
# the following conditions are met:
# * Redistributions of source code must retain the above copyright notice, this list of conditions and the
#   following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other materials provided with the distribution.
# * Neither the name of Clearpath Robotics nor the names of its contributors may be used to endorse or
#   promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rospy
import numpy as np
from geometry_msgs.msg import TwistStamped
from geometry_msgs.msg import TwistWithCovarianceStamped
from sensor_msgs.msg import NavSatFix

def navfix_cb(msg):
    covariance[0] = msg.position_covariance[0]
    covariance[7] = msg.position_covariance[4]
    covariance[14] = msg.position_covariance[8]

def navsat_cb(msg):
    global vel_pub
    global covariance

    new_msg = TwistWithCovarianceStamped()

    new_msg.header = msg.header
    new_msg.twist.twist = msg.twist
    new_msg.twist.covariance = covariance

    vel_pub.publish(new_msg)


def add_cov():
    global vel_pub
    global covariance

    rospy.init_node("navsat_vel_cov")

    navsat_sub = rospy.Subscriber("navsat/vel", TwistStamped, navsat_cb)
    navfix_sub = rospy.Subscriber("navsat/fix", NavSatFix, navfix_cb)
    vel_pub = rospy.Publisher("navsat/vel_cov", TwistWithCovarianceStamped, queue_size=1)

    covariance = list((10 * np.identity(6)).reshape((36,)))

    rospy.spin()

if __name__ == '__main__':
    add_cov()
