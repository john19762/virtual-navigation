# Virtual Navigation Path

#### 介绍
在真实地面上画线让机器人导航受光线限制，而且不利于最优路径规划，在机器人slam使用的栅格地图中设计导航路径，避免在真实地面上画线导航的缺点。

#### 软件架构
软件架构说明
本项目是在重德xbot-u智能机器人基础上开发的，重德机器人的源码参见https://gitee.com/zhoulijun1976/xbot-u链接。

#### 安装教程

1.  在项目https://gitee.com/zhoulijun1976/xbot-u基础上，将本项目中的\xbot\xbot_navi文件夹全部复制到https://gitee.com/zhoulijun1976/xbot-u项目中的\xbot文件夹下。

#### 使用说明
如果想使用虚拟障碍物构建出机器人活动空间实现导航，使用如下步骤：
1.  roslaunch xbot_navi xbot_virnav.launch
2.  roslaunch xbot_navi view_rviz.launch

如果想使用虚拟路径点导航，启动机器人后，运行roslaunch xbot_navi build_map.launch
1.运行rosrun xbot_navi zhouxbot_getpositon.py，记录机器人需要走的点
2.将机器人放在刚才机器人的起点
运行rosrun xbot_navi zhouxbot_publish_virnav.py 机器人即可按上一步存储的轨迹行走。
