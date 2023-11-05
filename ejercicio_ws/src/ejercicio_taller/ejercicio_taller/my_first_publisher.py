import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class NodeName(Node):
    def __init__(self) -> None:
        super().__init__('node_name')
        # Create Publishers
        self.example_publisher = self.create_publisher(String,"example_topic",10)

        # Create Subscribers

        # Initialize attributes
        self.counter = 0

        # Create timers
        self.timer = self.create_timer(1,self.timer_callback)

    # Create callback methods (subscribers and timers)
    def timer_callback(self):
        msg = String()
        msg.data = "Hello World" + str(self.counter)
        self.example_publisher.publish(msg)
        self.counter += 1

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