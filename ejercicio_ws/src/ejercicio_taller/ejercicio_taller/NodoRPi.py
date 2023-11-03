import RPi.GPIO as GPIO
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from std_msgs.msg import Int32, Float32, Bool


class NodeName(Node):
    def __init__(self) -> None:
        super().__init__('node_name')

        qos_profile = QoSProfile(
            reliability = ReliabilityPolicy.BEST_EFFORT,
            durability = DurabilityPolicy.TRANSIENT_LOCAL,
            history = HistoryPolicy.KEEP_LAST,
            depth = 1
        )

        # Create Publishers
        self.publisher_proxomidad = self.create_publisher(Float32, "/distancia_sensor",qos_profile)
        self.publisher_boton = self.create_publisher(Bool, "/estado_boton",qos_profile)

        # Create Subscribers
        self.subscriber_LED = self.create_subscription(Bool,"/estado_LED",self.callback_sub_LED,qos_profile)
        self.subscriber_servo = self.create_subscription(Int32,"/pwm_servo", self.callback_sub_servo,qos_profile)
        # Initialize attributes

        # Create timers
    def callback_sub_LED(self):
        pass

    def callback_sub_servo(self):
        pass
    # Create callback methods (subscribers and timers)

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