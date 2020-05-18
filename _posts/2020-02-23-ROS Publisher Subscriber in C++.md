---
title: "ROS publisher subscriber in C++"
date: 2020-02-23 00:26:00 +0800
categories: [ROS C++]
tags: [ROS C++]
---

So I had to develop the ROS publisher and Subscriber and in C++. So what ROS already gives this tutorial so why a need for my rip off? Well well well

I am writing everything in OOP's C++ way. There are a lot of problems come down the road. The first problem is of setting up your IDE to support ROS. Fortunately I use CLion. They have a wonderful tutorial on how to set it up. Fair enough. 

https://www.jetbrains.com/help/clion/ros-setup-tutorial.html

Apart from that some tips:

- Activate the catkin environment first and then run in the terminal the clion.sh from the appropriate path where you installed CLion. Don't run it from Desktop entry, you will get weird problems, so run it directly from terminal. If you still think it's a lot of hassle, you can run it in the screen and then close it. 

Next For every individual small part you make, make a folder and make personal CmakeLists.txt for it. Finally include it in the main Project level CmakeLists.txt using

```cmake
add_subdirectory(RELATIVE_PATH_TO_YOUR_SUB_PROJECT)

```

Now you can edit this CMakeLists.txt ratrher editing the global one. This will also give you more power to comment some sub projects out if you need.

Next my CMakeLists.txt looked something like this:

```cmake
cmake_minimum_required(VERSION 3.13)
project(PoseEstimation)
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs imu_filter_madgwick)
set(CMAKE_CXX_STANDARD 14)
include_directories(/opt/ros/melodic/include)
add_executable(PoseEstimation main.cpp PoseEstimationPublisher.cpp PoseEstimationPublisher.h)
target_link_libraries(PoseEstimation ${catkin_LIBRARIES})
install(TARGETS PoseEstimation DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
```

So in here you specify all the catkin components you need. Make sure these requirements are synchronized with catkin package's package.xml requiremnts, so that others can directly install the dependencies using rosdep install. Finally you need to mention the install clause because that will help installing the binaries in correct place so that you can run rosrun and run the binaries. Advantage is that you can also mention everything in launch file. For example to run this you need:

```bash
rosrun ros_robotic_skin PoseEstimation
```

Where ros_robotic_skin is the catkin_package and PoseEstimation is the compiled binary. Now you also run this in launch file by writing this line in your launch file:

```xm
<node name="PoseEstimationPublisher" pkg="ros_robotic_skin" type="PoseEstimation" />
```

The node name can be literally anything. 

Now let's go through the original ROS documentation code:

[http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber(c%2B%2B))

Read this before reading the anything below further, as I don't explain everything in here.

Now that all is setup let's look into the code:

```c++
#include "PoseEstimationPublisher.h"
#include <imu_filter_madgwick/imu_filter.h>
#define FILTER_ITERATIONS 10000

/*
 * The below part filterStationary is directly copied from imu_filter_madgwick example file:
 * https://github.com/ccny-ros-pkg/imu_tools/blob/indigo/imu_filter_madgwick/test/madgwick_test.cpp
 * */
template <WorldFrame::WorldFrame FRAME>
void filterStationary(
        float Ax, float Ay, float Az,
        float Mx, float My, float Mz,
        double& q0, double& q1, double& q2, double& q3) {
    float dt = 0.1;
    float Gx = 0.0, Gy = 0.0, Gz = 0.0; // Stationary state => Gyro = (0,0,0)

    ImuFilter filter;
    filter.setDriftBiasGain(0.0);
    filter.setAlgorithmGain(0.1);

    // initialize with some orientation
    filter.setOrientation(q0,q1,q2,q3);
    filter.setWorldFrame(FRAME);

    for (int i = 0; i < FILTER_ITERATIONS; i++) {
        filter.madgwickAHRSupdate(Gx, Gy, Gz, Ax, Ay, Az, Mx, My, Mz, dt);
    }

    filter.getOrientation(q0,q1,q2,q3);
}

template <WorldFrame::WorldFrame FRAME>
void filterStationary(float Ax, float Ay, float Az,
                      double& q0, double& q1, double& q2, double& q3) {
    float dt = 0.1;
    float Gx = 0.0, Gy = 0.0, Gz = 0.0; // Stationary state => Gyro = (0,0,0)

    ImuFilter filter;
    filter.setDriftBiasGain(0.0);
    filter.setAlgorithmGain(0.1);

    // initialize with some orientation
    filter.setOrientation(q0,q1,q2,q3);
    filter.setWorldFrame(FRAME);

    for (int i = 0; i < FILTER_ITERATIONS; i++) {
        filter.madgwickAHRSupdateIMU(Gx, Gy, Gz, Ax, Ay, Az, dt);
    }

    filter.getOrientation(q0,q1,q2,q3);
}



void PosePublisher::init() {
    // Here just starting the function which will initialize the callback from different IMU placed on Franka
    get_imu_data();

}

void PosePublisher::get_imu_data() {
    // Loop through IMU numbers and subscribe to them with static class function imu_callback
    std::vector<int> imu_numbers {1, 2, 3, 4, 5, 6, 7};
    for(int i: imu_numbers){
        ros::Subscriber cam_sub = nh->subscribe("/imu_data"+std::to_string(i),100, imu_callback);
    }
    ros::spin();
}

void PosePublisher::imu_callback(const sensor_msgs::Imu::ConstPtr &msg) {
    double q0, q1, q2, q3;
    filterStationary<WorldFrame::NED>((float)msg->linear_acceleration.x, (float)msg->linear_acceleration.y, (float)msg->linear_acceleration.z,
                                      (float)msg->angular_velocity.x, (float)msg->angular_velocity.y, (float)msg->angular_velocity.z,
                                      q0, q1, q2, q3);
    geometry_msgs::Quaternion calculated_quaternion;
    /*Why considering like that?:
     * Proof: https://github.com/ccny-ros-pkg/imu_tools/blob/indigo/imu_filter_madgwick/src/imu_filter_ros.cpp#L297
     * */
    calculated_quaternion.x = q1;
    calculated_quaternion.y = q2;
    calculated_quaternion.z = q3;
    calculated_quaternion.w =  q0;
    /*
     * Writing like this has two reasons
     * 1) You cannot re initialize imu0_pose and publish to it, when done in a loop nothing gets published and also
     * the topic isn't visible. Basically you can't initialize like this PosePublisher::nh->advertise<geometry_msgs::Quaternion>("imu0_pose", 100) again and again and publish to it
     * Hence the reason of hardcoding
     *
     * 2) This will make it fast rather than initializing again and again
     *
     * 3) Using if-else if will make it easier to read rather than switch
     * */
    if(msg->header.frame_id == "imu_data0"){
        imu0_pose.publish(calculated_quaternion);
    } else if(msg->header.frame_id == "imu_data1"){
        imu1_pose.publish(calculated_quaternion);
    } else if(msg->header.frame_id == "imu_data2"){
        imu2_pose.publish(calculated_quaternion);
    } else if(msg->header.frame_id == "imu_data3"){
        imu3_pose.publish(calculated_quaternion);
    } else if(msg->header.frame_id == "imu_data4"){
        imu4_pose.publish(calculated_quaternion);
    } else if(msg->header.frame_id == "imu_data5"){
        imu5_pose.publish(calculated_quaternion);
    } else if(msg->header.frame_id == "imu_data6"){
        imu6_pose.publish(calculated_quaternion);
    } else if(msg->header.frame_id == "imu_data7"){
        imu7_pose.publish(calculated_quaternion);
    }

}
```

The header file:

```c++
#ifndef POSEESTIMATION_POSEESTIMATIONPUBLISHER_H
#define POSEESTIMATION_POSEESTIMATIONPUBLISHER_H
#include "ros/ros.h"
#include "trajectory_msgs/JointTrajectory.h"
#include "trajectory_msgs/JointTrajectoryPoint.h"
#include "sensor_msgs/Imu.h"
#include "geometry_msgs/Quaternion.h"

class PosePublisher {
    // This class is made so that everything required can be encapsulated in one class
public:
    /*Why pointer to a node handle? Because you initialize it in the main function only
     * and next pass on to other functions to use it*/
    static ros::NodeHandle* nh;
    /*Below are static ROS Publishers*/
    static ros::Publisher imu0_pose;
    static ros::Publisher imu1_pose;
    static ros::Publisher imu2_pose;
    static ros::Publisher imu3_pose;
    static ros::Publisher imu4_pose;
    static ros::Publisher imu5_pose;
    static ros::Publisher imu6_pose;
    static ros::Publisher imu7_pose;
    static void init();
    static void get_imu_data();
    static void imu_callback(const sensor_msgs::Imu::ConstPtr& msg);

};


#endif //POSEESTIMATION_POSEESTIMATIONPUBLISHER_H
```

And the main file:

```c++
#include "PoseEstimationPublisher.h"

ros::NodeHandle* PosePublisher::nh;
ros::Publisher PosePublisher::imu0_pose;
ros::Publisher PosePublisher::imu1_pose;
ros::Publisher PosePublisher::imu2_pose;
ros::Publisher PosePublisher::imu3_pose;
ros::Publisher PosePublisher::imu4_pose;
ros::Publisher PosePublisher::imu5_pose;
ros::Publisher PosePublisher::imu6_pose;
ros::Publisher PosePublisher::imu7_pose;
int main(int argc, char** argv) {
    ros::init(argc,argv,"IMU_Pose_Estimator");
    // Declaring the ROS Handle in main and passing the pointer to it around to other classes to use it
    ros::NodeHandle nhp;
    PosePublisher::nh = &nhp;
    PosePublisher::imu0_pose = PosePublisher::nh->advertise<geometry_msgs::Quaternion>("imu0_pose", 100);
    PosePublisher::imu1_pose = PosePublisher::nh->advertise<geometry_msgs::Quaternion>("imu1_pose", 100);
    PosePublisher::imu2_pose = PosePublisher::nh->advertise<geometry_msgs::Quaternion>("imu2_pose", 100);
    PosePublisher::imu3_pose = PosePublisher::nh->advertise<geometry_msgs::Quaternion>("imu3_pose", 100);
    PosePublisher::imu4_pose = PosePublisher::nh->advertise<geometry_msgs::Quaternion>("imu4_pose", 100);
    PosePublisher::imu5_pose = PosePublisher::nh->advertise<geometry_msgs::Quaternion>("imu5_pose", 100);
    PosePublisher::imu6_pose = PosePublisher::nh->advertise<geometry_msgs::Quaternion>("imu6_pose", 100);
    PosePublisher::imu7_pose = PosePublisher::nh->advertise<geometry_msgs::Quaternion>("imu7_pose", 100);
    PosePublisher::init();
    return 0;
}
```

The main problem I want to discuss is that you can only initialize ros::NodeHandle once in the program and use it to publish the data. Also it cannot be initialized before ros::init. It cannot be initialized again and again in callback function. You shouldn't make it a global variable as it's a bad practise. So what to do?

You initialize the ros::NodeHandle in main, and pass around it's pointer to other classes and functions like I did in main and bam!

Enjoy!!