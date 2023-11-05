# Abre y cierra la puerta cada vez que se oprime el boton
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool, String
import time

class NodeName(Node):
    def __init__(self) -> None:
        super().__init__('node_name')

        # Create Publishers
        self.publisher_servo = self.create_publisher(String,"/pwm_servo",10)

        # Create Subscribers
        self.subscriber_boton = self.create_subscription(Bool,"/estado_boton",self.callback_boton,1)

        # Inicializar servo
        inicio = String()
        inicio.data = "CERRAR"
        self.publisher_servo.publish(inicio)

    def callback_boton(self,msg):
        msg_servo = String()
        if (msg.data): # verificar presion de boton
            msg_servo.data = "ABRIR"
            self.publisher_servo.publish(msg_servo)
            time.sleep(2)
            msg_servo.data = "CERRAR"
            self.publisher_servo.publish(msg_servo)

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