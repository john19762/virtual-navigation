#!/usr/bin/env python
#coding=utf-8


import rospy,os,json,time

from std_msgs.msg import String, UInt32, UInt8, Bool
from geometry_msgs.msg import Pose, PoseStamped
from actionlib_msgs.msg import GoalStatusArray
from move_base_msgs.msg import MoveBaseActionResult
from std_srvs.srv import Empty
ws_path = os.popen('rospack find xbot_navi').read().strip()  #navigation_sim_demo工作区路径
json_file_address = ws_path + '/map/kp.json'
class demo():
    """docstring for welcome"""
    def __init__(self):
#       声明节点订阅与发布的消息

        # 发布目标点信息
        self.move_base_goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
        # 订阅是否到达目标点结果
        self.move_base_result_sub = rospy.Subscriber('/move_base/result', MoveBaseActionResult, self.move_base_resultCB)
        # 请求清除costmap服务
        self.clear_costmaps_srv = rospy.ServiceProxy('/move_base/clear_costmaps',Empty)

#        记录机器人当前的目标点
        self.current_goal = 0

#        读取一存储的讲解点字典文件,默认位于xbot_s/param/position_dic.yaml文件
        self.kp_path = rospy.get_param('/demo/kp_path',json_file_address)
        with open(self.kp_path, 'r') as json_file:
            self.kp_list = json.load(json_file)
        json_file.close()
        rospy.spin()

    def pub_kp(self):
        if self.current_goal < len(self.kp_list):
            pos = self.kp_list[self.current_goal]['pose']
            goal = PoseStamped()
            goal.header.frame_id = 'map'
            goal.pose.position.x = pos[0][0]
            goal.pose.position.y = pos[0][1]
            goal.pose.position.z = pos[0][2]
            goal.pose.orientation.x = pos[1][0]
            goal.pose.orientation.y = pos[1][1]
            goal.pose.orientation.z = pos[1][2]
            goal.pose.orientation.w = pos[1][3]

            self.move_base_goal_pub.publish(goal)

#    导航程序对前往目标点的执行结果
    def move_base_resultCB(self, result):
        print("move_base_resultCB"+str(result))
        if result.status.status == 3:
#            成功到达目标点
            kp = self.kp_list[self.current_goal]
            self.current_goal += 1
            self.clear_costmaps_srv()
            self.pub_kp()
        elif result.status.status == 4:
#            到达目标点失败,slam发布abort信号给talker,talker会请求前方人员让一下,然后重新规划路径尝试去往目标点
            self.pub_kp()


if __name__ == '__main__':
    rospy.init_node('demo_node')
    try:
        rospy.loginfo('demo node initialized...')
        demo()
    except rospy.ROSInterruptException:
        rospy.loginfo('demo node initialize failed, please retry...')
