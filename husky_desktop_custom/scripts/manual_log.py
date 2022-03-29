#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/sickness_log', String, queue_size=1)
    rospy.init_node('sickness_logger', anonymous=True)

    while not rospy.is_shutdown():
        log_entry = str(raw_input("Enter messsage: "))
        log_str = String(log_entry)
        pub.publish(log_str)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        print "ROS shutdown request - exiting"
        exit()
    except KeyboardInterrupt:
        print "Keyboard interrupt - exiting"
        exit()