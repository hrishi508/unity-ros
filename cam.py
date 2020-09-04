#!/usr/bin/env python2
import rospy, cv2, cv_bridge
from sensor_msgs.msg import Image


class Img:
	def __init__(self):
		self.bridge = cv_bridge.CvBridge()
		cv2.namedWindow("image1", 1)
		self.image_sub = rospy.Subscriber('a',Image,self.image_callback)
		
	
	def image_callback(self, msg):
		image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
		cv2.imshow("image1", image)
		cv2.waitKey(3)


rospy.init_node('cam')
cam = Img()
rospy.spin()

