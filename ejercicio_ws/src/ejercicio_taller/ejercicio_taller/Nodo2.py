# Prende el LED si hay alguien cerca
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float32
import time

class Nodo2(Node):
    def __init__(self) -> None:
        super().__init__('Nodo2')

        # Create Publishers
        self.publisher_LED = self.create_publisher(Bool,"estado_LED",10)

        # Create Subscribers
        self.subscriber_proximidad = self.create_subscription(Float32,"/distancia_sensor",self.callback_distancia,10)

    # Create callback methods (subscribers and timers)
    def callback_distancia(self,msg):
        distancia = msg.data
        msg_LED = Bool()
        if (distancia < 10.0):
            msg_LED.data = True
        else: msg_LED.data = False
        self.publisher_LED.publish(msg_LED)

def main(args=None) -> None:
    rclpy.init(args=args)
    node_name= Nodo2()
    rclpy.spin(node_name)
    node_name.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)