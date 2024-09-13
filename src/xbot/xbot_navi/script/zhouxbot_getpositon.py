#!/usr/bin/env python
#coding=utf-8
import tf
import rospy
import json,os

ws_path = os.popen('rospack find xbot_navi').read().strip()  #navigation_sim_demo工作区路径
json_file = ws_path + '/map/kp.json'

def get_robot_pose():
    listener = tf.TransformListener()
    rospy.sleep(1)  # 等待tf树初始化

    try:
        (trans, rot) = listener.lookupTransform('/odom', '/base_footprint', rospy.Time(0))
        return trans, rot
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        return None

if __name__ == '__main__':
    rospy.init_node('get_robot_pose')
    count=30
    kp = []
    while count>0:
        pose = get_robot_pose()
        count=count-1
        kptmp = {"pose": [pose[0],pose[1]]}
        kp.append(kptmp)
        rospy.sleep(1)  # 等待1秒
    with open(json_file, 'w') as f:
    	json.dump(kp,f,ensure_ascii=False)
