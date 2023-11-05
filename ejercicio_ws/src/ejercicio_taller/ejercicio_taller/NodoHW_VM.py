import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool, String
import time

class Nodo1(Node):
    def __init__(self) -> None:
        super().__init__('NodoHW_VM')

        # Create Subscribers
        self.publisher_test = self.create_publisher(String,"/topic_test",10)
        self.text = ["Viva IEEE RAS", "Viva el T-RC"]
        self.index = 0

        self.timer = self.create_timer(0.5,self.callback_test)

    def callback_test(self,msg):
        msg_test = String()
        self.index = not(self.index)
        msg_test.data = self.text[self.index]
        self.publisher_test(msg_test)

def main(args=None) -> None:
    rclpy.init(args=args)
    node_name= Nodo1()
    rclpy.spin(node_name)
    node_name.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)