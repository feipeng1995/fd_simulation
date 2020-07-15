#!/usr/bin/env python
# coding=utf-8
# publish the velocity to the cmd_vel
import time
import rospy
import numpy
from geometry_msgs.msg import Twist
# import scipy.io as scio
# datafile = 'usvmodel.mat'
# data = scio.loadmat(datafile)
# data = numpy.load('linearx1.npy')
# real data
#data = [0.04, 0.08, -0.06, -0.2, -0.34, -0.48, -0.62, -0.76, -0.89, -1.03, -1.15, -1.27, -1.38, -1.47, -1.55, -1.61, -1.64, -1.65, -1.62, -1.36, -1.13, -0.91, -0.7, -0.53, -0.41, -0.31, -0.23, -0.11, 0.01, 0.09, 0.16, 0.2, 0.24, 0.26, 0.27, 0.26, 0.26, 0.24, 0.22, 0.2, 0.18, 0.15, 0.12, 0.09, 0.07, 0.05, 0.02, -0.04, -0.04, -0.03, -0.03, -0.02, -0.02, -0.01, 0.05, 0.1, 0.16, 0.18, 0.21, 0.19, 0.12, 0.14, 0.07, 0.04, 0.0, -0.01, -0.03, -0.05, -0.06, -0.06, -0.07, -0.08, -0.08, -0.08, -0.08, -0.08, -0.07, -0.07, -0.06, -0.06, -0.05, -0.05, -0.05, -0.05, -0.04, -0.04, -0.04, -0.04, -0.03, -0.03, -0.03, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.0, -0.0, -0.0, 0.0, 0.0, 0.01, 0.01, 0.01, 0.0, -0.01, -0.02, -0.04, -0.04, -0.05, -0.05, -0.05, -0.06, -0.06, -0.09, -0.05, -0.1, -0.06, -0.05, -0.09, -0.07, -0.08, -0.12, -0.16, -0.2, -0.19, -0.15, -0.15, -0.18, -0.2, -0.22, -0.27, -0.31, -0.33, -0.34, -0.35, -0.34, -0.33, -0.28]
# print type(data)
data = [0.04, -0.1, -0.25, -0.39, -0.53, -0.67, -0.81, -0.96, -1.09, -1.23, -1.36, -1.48, -1.59, -1.69, -1.79, -1.81, -1.83, -1.85, -1.75, -1.66, -1.48, -1.29, -1.13, -0.98, -0.84, -0.71, -0.58, -0.47, -0.37, -0.27, -0.19, -0.11, -0.05, -0.0, 0.03, 0.06, 0.08, 0.09, 0.1, 0.1, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.02, 0.01, 0.01, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.0, 0.0, 0.0, 0.0, -0.0, -0.0, -0.01, -0.01, -0.01, -0.02, -0.02, -0.02, -0.03, -0.03, -0.03, -0.03, -0.04, -0.04, -0.04, -0.04, -0.03, -0.03, -0.03, -0.03, -0.03, -0.03, -0.03, -0.02, -0.02, -0.02, -0.02, -0.01, -0.01, -0.01, -0.0, -0.0, 0.0, 0.01, 0.01, 0.01, -0.01, -0.03, -0.05, -0.06, -0.12, -0.09, -0.07, -0.05, -0.05, -0.06, -0.1, -0.08, -0.12, -0.09, -0.07, -0.05, -0.07, -0.09, -0.12, -0.17, -0.16, -0.15, -0.17, -0.2, -0.22, -0.24, -0.33, -0.3, -0.26, -0.28, -0.27, -0.26, -0.24, -0.13, -0.13]
def velocity_publisher():
    #init node
    rospy.init_node('velocity_publisher', anonymous=True)
    #creat a publisher, publish the topic /cmd_vel， msg: geometry_msgs:Twist, The queue length is ten
    pub = rospy.Publisher('cmd_vel',Twist,queue_size=10)
    #set cycle frequency
    rate = rospy.Rate(1)
    i=0
    while not rospy.is_shutdown():
        for i in range(150):
        #agent 2 state
            linearx = float(data[i])
        # lineary = float(data['Trajectory'][1][i][4])
            angularz = 0
            vel_msg = Twist()
            vel_msg.linear.x= linearx
        # vel_msg.linear.y= lineary
            vel_msg.angular.z= angularz
        #publish the msg
            pub.publish(vel_msg)
            rospy.loginfo("publish usv velocity command[%0.2f m/s,%0.2f m/s, %0.2f rad/s]",vel_msg.linear.x,vel_msg.linear.y,vel_msg.angular.z)
        #delay as the cycle frequency
        # time.sleep(0.1)
            rate.sleep()
    # rospy.signal_shutdown('form formation')
if __name__== '__main__':
    # try:
    #     velocity_publisher()
    # except rospy.ROSInternalException:
    #     pass
    while  True:
        velocity_publisher()
    # try:
    #     velocity_publisher()
    
    # except rospy.ROSInternalException:
    #     pass
