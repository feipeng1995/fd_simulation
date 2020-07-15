# fd_simulation
无人艇仿真环境搭建(参考ros development studio)
命令顺序：
mkdir -p /home/puffet/tutorial_ws/src
cd /home/puffet/tutorial_ws/
catkin_make
#copy files

#install depen
rosdep install --from-paths /home/puffet/tutorial_ws --ignore-src --rosdistro=kinetic
catkin_make
#demo 1
source devel/setup.bash
rospack profile
roslaunch robotx_gazebo sandisland.launch
#demo2
cd src
#git clone https://bitbucket.org/theconstructcore/spawn_robot_tools.git
git clone https://RDaneelolivaw@bitbucket.org/theconstructcore/spawn_robot_tools.git
catkin_make
roslaunch wamv_openai_ros_example start_training.launch 
报错，需要安装gym https://blog.csdn.net/aozhipujian10997/article/details/86607389
参考视频：https://www.theconstructsim.com/ros-qa-153-use-rosjects-locally/
