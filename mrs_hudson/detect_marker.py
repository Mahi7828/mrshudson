from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import rclpy
from rclpy.node import Node
import cv2.aruco as aruco
import numpy as np

class ArUcoDetector(Node):
    def __init__(self):
        super().__init__('detect_marker')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/turtlebot3_waffle_pi/camera/image_raw',
            self.callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def detect_ArUco(self, img):
        Detected_ArUco_markers = {}
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
        parameters = aruco.DetectorParameters_create()

        corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        i = 0
        try:
            for id in ids:
                for id_Number in id:
                    Detected_ArUco_markers[id_Number] = corners[i][0]
        except TypeError:
            self.get_logger().info("No aruco in front of me")

        i += 1
        return Detected_ArUco_markers

    def mark_ArUco(self, img, Detected_ArUco_markers):
        ids = Detected_ArUco_markers.keys()
        centre_aruco = {}
        top_centre = {}

        try:
            for id in ids:
                corners = Detected_ArUco_markers[id]
                for i in range(0, 4):
                    cv2.circle(img, (int(corners[i][0]), int(corners[i][1])), 5, (0, 0, 255), -1)
                centre_aruco[id] = (corners[0] + corners[1] + corners[2] + corners[3]) / 4
                top_centre[id] = (corners[0] + corners[1]) / 2
                cv2.line(img, (int(centre_aruco[id][0]), int(centre_aruco[id][1])),
                         (int(top_centre[id][0]), int(top_centre[id][1])), (255, 0, 0), 5)

        except TypeError:
            self.get_logger().info("No aruco in front of me")

        return img

    def callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            self.get_logger().error("CvBridge Error: {0}".format(e))

        Detected_ArUco_markers = self.detect_ArUco(cv_image)
        img = self.mark_ArUco(cv_image, Detected_ArUco_markers)
        cv2.imshow("Image Window", img)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    try:
        node = ArUcoDetector()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
