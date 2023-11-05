import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class NodeName(Node):
    def __init__(self) -> None:
        super().__init__('node_name')
        # Create Publishers
        # Create Subscribers
        self.example_subscriber = self.create_subscription(String,"example_topic",self.subscriber_callback,10)

    # Create callback methods (subscribers and timers)
    def subscriber_callback(self,msg):
        msg_received = msg.data
        self.get_logger().info("Message recieved: " + msg_received)

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