from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    usb_cam_node = Node(
        package='usb_cam',
        executable='usb_cam_node_exe',
        name='usb_cam'
    )

    image_converter_node = Node(
        package='image_conversion_pkg',
        executable='image_conversion_node',
        name='image_conversion_node'
    )

    return LaunchDescription([
        usb_cam_node,
        image_converter_node
    ])
