import RPi.GPIO as GPIO
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool, String

class NodoRPi(Node):
    def __init__(self) -> None:
        super().__init__('NodoHW_RPi')
        self.subscriber_test = self.create_subscription(String,"/topic_test",self.callback_sub_test,10)

    def callback_sub_test(self,msg):
        self.get_logger().info(msg.data)

def main(args=None) -> None:
    rclpy.init(args=args)
    nodo = NodoRPi()
    rclpy.spin(nodo)
    GPIO.cleanup()
    nodo.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)