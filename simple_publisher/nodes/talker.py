#!/usr/bin/env python
# Required before starting our code
from venv_utils import activate_virtual_env
venv_status = activate_virtual_env()

import rospy
from std_msgs.msg import String
import tensorflow as tf


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print("Tensorflow version is {}".format(tf.__version__))
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
