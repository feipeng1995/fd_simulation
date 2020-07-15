#!/usr/bin/env python
# coding=utf-8
# publish the velocity to the cmd_vel
import rospy
from geometry_msgs.msg import Twist
import time
def velocity_publisher():
    #init node
    rospy.init_node('velocity_publisher', anonymous=True)
    #creat a publisher, publish the topic /cmd_vel， msg: geometry_msgs:Twist, The queue length is ten
    pub = rospy.Publisher('cmd_vel',Twist,queue_size=10)
    #set cycle frequency
    rate = rospy.Rate(10)
    linearx = -1.0
    while not rospy.is_shutdown():
        for i in range(150): 
            vel_msg = Twist()
            vel_msg.linear.x= linearx
            vel_msg.angular.z= 0
            #publish the msg
            pub.publish(vel_msg)
            rospy.loginfo("publish usv velocity command[%0.2f m/s, %0.2f rad/s]",vel_msg.linear.x,vel_msg.angular.z)
            #delay as the cycle frequency
            rate.sleep()
            # time.sleep(0.1)
    #shut down the node
    # rospy.signal_shutdown('form formation')
if __name__== '__main__':
    try:
        # linearx = 2.0
        # for i in range(10):
        #     if linearx>= 0:
        #         linearx = linearx-0.5
        #     else:
        #         break
        #     velocity_publisher()
        #     time.sleep(1)
        velocity_publisher()
        # velocity_publisher()
    except rospy.ROSInternalException:
        pass


