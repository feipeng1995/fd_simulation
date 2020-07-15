#!/usr/bin/env python


import rospy
from geometry_msgs.msg import PoseStamped
from gazebo_msgs.msg import ModelStates
from std_msgs.msg import Header
import numpy as np
import tf
from geometry_msgs.msg import Quaternion
# publish topic"mavros/vision_oose/pose"
pub = rospy.Publisher('mavros/vision_pose/pose', PoseStamped, queue_size=1)

sequence = 0
i = 0


def gazeboCallBack(data, model_name):
    # print data.pose[1].position
    global sequence
    global i

    i += 1
    # while i == 5 
    if i % 5 == 0:

        pose = data.pose[data.name.index(model_name)]
	
	# mavros_extras 0.18.7 has included the transform bellow
        # r - imu frame (FLU)
        # b - px4 body frame (FRD)
        # g - gazebo ENU frame
        #q_gr = np.array([pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w])
        #q_br = np.array([1, 0, 0, 0])
        #q_gb = tf.transformations.quaternion_multiply(q_gr, tf.transformations.quaternion_conjugate(q_br))
        #pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w = q_gb

        header = Header()

        header.seq = sequence
        sequence += 1
        header.stamp = rospy.Time.now()

        pub.publish(header, pose)


def positionBroadcast():
    rospy.init_node('LPS', anonymous=False)

    while not rospy.has_param('~model_name'): # while no param, wait.
        pass

    model_name = rospy.get_param('~model_name')

    assert isinstance(model_name, str) #
    rospy.Subscriber("/gazebo/model_states", ModelStates, gazeboCallBack, model_name)

    rospy.spin()


if __name__ == '__main__':
    positionBroadcast()
