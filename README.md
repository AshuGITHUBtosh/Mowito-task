## Camera Toggle
This project implements a ROS2 package for image conversion using a live camera feed.
The node subscribes to images from the usb_cam package, converts them to grayscale or color based on a service call, and publishes the converted images to a new ROS2 topic.

The system also displays the processed image using OpenCV for real-time visualization.




## Tools used
 - ROS2 Humble
 - OpenCV
 - cv_bridge
 - usb_cam

## Dependencies & Installation
### Install ROS2 on Ubuntu
- ```sudo apt install ros-humble-desktop```
- ```source /opt/ros/humble/setup.bash```
### Install Python Dependencies
- ```pip install opencv-python numpy scipy```

### Install ROS2 Packages
- ```sudo apt update && sudo apt install ros-humble-vision-msgs ros-humble-cv-bridge python3-numpy```

 ## Execution
 - ``` colcon build ```
 - ``` source install/setup.bash```
 - ```ros2 launch image_conversion_pkg image_conversion_launch.py ```
 - ``` ros2 service call /set_grayscale_mode std_srvs/srv/SetBool "{data: true}"```
 - ``` ros2 service call /set_grayscale_mode std_srvs/srv/SetBool "{data: flase}"```




   
 
