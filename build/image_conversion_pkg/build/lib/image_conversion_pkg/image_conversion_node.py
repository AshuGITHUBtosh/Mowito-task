import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from std_srvs.srv import SetBool

from cv_bridge import CvBridge
import cv2


class ImageConversionNode(Node):

    def __init__(self):
        super().__init__('image_conversion_node')

        self.bridge = CvBridge()

        # False = Color, True = Grayscale
        self.mode = False

        # Subscriber
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.image_callback,
            10)

        # Publisher
        self.publisher = self.create_publisher(
            Image,
            '/converted_image',
            10)

        # Service
        self.service = self.create_service(
            SetBool,
            'set_grayscale_mode',
            self.service_callback)

        self.get_logger().info("Image Conversion Node Started")


    def service_callback(self, request, response):

        self.mode = request.data

        if self.mode:
            self.get_logger().info("Switched to GRAYSCALE mode")
        else:
            self.get_logger().info("Switched to COLOR mode")

        response.success = True
        response.message = "Mode changed"

        return response


    def image_callback(self, msg):

        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        if self.mode:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        # Publish
        out_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher.publish(out_msg)

        # Display window
        cv2.imshow("Converted Image", frame)
        cv2.waitKey(1)


def main(args=None):

    rclpy.init(args=args)

    node = ImageConversionNode()

    rclpy.spin(node)

    node.destroy_node()

    cv2.destroyAllWindows()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
