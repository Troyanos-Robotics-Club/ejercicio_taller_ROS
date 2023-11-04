#import RPi.GPIO as GPIO
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class NodeName(Node):
    def __init__(self) -> None:
        super().__init__('node_name')

        # Create Publishers
        self.test_publisher = self.create_publisher(String,"/topic_test",10)

        # Create Subscribers

        # Initialize attributes

        # Create timers
        self.timer1 = self.create_timer(1,self.callback_timer)

    # Create callback methods (subscribers and timers)
    def callback_timer(self):
        msg = String()
        msg.data = "nice"
        self.test_publisher.publish(msg)

def main(args=None) -> None:
    rclpy.init(args=args)
    node_name= NodeName()
    rclpy.spin(node_name)
    node_name.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)